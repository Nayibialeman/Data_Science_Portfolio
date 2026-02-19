# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 20:20:02 2025
streamlit run blockbuster_nft.py
pip install streamlit pymongo pandas
@author: alema
"""

import streamlit as st
from pymongo import MongoClient
from datetime import datetime, timedelta
import pandas as pd

# Configuración de Streamlit
st.set_page_config(page_title="🎬 Blockbuster NFT", page_icon="🧾")

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Token"]
collection = db["nofung"]

# Menú
menu = st.sidebar.selectbox("📋 Menú", ["Registrar película", "Rentar", "Devolver", "Historial", "Vencimientos próximos"])

# Registrar película
if menu == "Registrar película":
    st.title("🎥 Registro de película como NFT")
    token_id = st.text_input("ID único del token (NFT)")
    pelicula = st.text_input("Nombre de la película")

    if st.button("Registrar"):
        existe = collection.find_one({"token_id": token_id})
        if existe:
            st.warning("⚠️ Este token ya existe.")
        else:
            collection.insert_one({
                "token_id": token_id,
                "pelicula": pelicula,
                "estado": "disponible"
            })
            st.success("✅ Película registrada correctamente.")

# Rentar
elif menu == "Rentar":
    st.title("📀 Rentar una película")
    cliente = st.text_input("Nombre del cliente")
    token_id = st.text_input("Token ID de la película")
    dias = st.number_input("Días de renta", min_value=1, max_value=30, value=3)

    if st.button("Rentar"):
        peli = collection.find_one({"token_id": token_id, "estado": "disponible"})
        if peli:
            collection.update_one(
                {"token_id": token_id},
                {"$set": {
                    "cliente": cliente,
                    "fecha_renta": datetime.utcnow(),
                    "fecha_vencimiento": datetime.utcnow() + timedelta(days=dias),
                    "estado": "rentado"
                }}
            )
            st.success(f"✅ {peli['pelicula']} fue rentada a {cliente}.")
        else:
            st.error("❌ Esta película no está disponible.")

# Devolver
elif menu == "Devolver":
    st.title("📤 Devolver película")
    token_id = st.text_input("Token ID de la película a devolver")

    if st.button("Devolver"):
        peli = collection.find_one({"token_id": token_id, "estado": "rentado"})
        if peli:
            collection.update_one(
                {"token_id": token_id},
                {"$set": {
                    "estado": "devuelto"
                }}
            )
            st.success(f"✅ {peli['pelicula']} fue devuelta con éxito.")
        else:
            st.warning("⚠️ La película ya fue devuelta o no existe.")

# Historial
elif menu == "Historial":
    st.title("🧾 Historial de películas")
    data = list(collection.find())
    if data:
        df = pd.DataFrame(data)
        df["fecha_renta"] = pd.to_datetime(df["fecha_renta"], errors='coerce')
        df["fecha_vencimiento"] = pd.to_datetime(df["fecha_vencimiento"], errors='coerce')
        st.dataframe(df[["token_id", "pelicula", "cliente", "estado", "fecha_renta", "fecha_vencimiento"]])
    else:
        st.info("No hay películas registradas aún.")

# Vencimientos próximos
elif menu == "Vencimientos próximos":
    st.title("⏳ Rentas por vencer (próximos 3 días)")
    hoy = datetime.utcnow()
    futuro = hoy + timedelta(days=3)
    vencimientos = list(collection.find({
        "estado": "rentado",
        "fecha_vencimiento": {"$lte": futuro}
    }))

    if vencimientos:
        df = pd.DataFrame(vencimientos)
        df["fecha_vencimiento"] = pd.to_datetime(df["fecha_vencimiento"])
        df["días_restantes"] = (df["fecha_vencimiento"] - hoy).dt.days
        st.dataframe(df[["pelicula", "cliente", "fecha_vencimiento", "días_restantes"]])
    else:
        st.success("✅ No hay rentas por vencer en los próximos 3 días.")