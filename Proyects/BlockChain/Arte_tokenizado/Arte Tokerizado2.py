# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 18:50:41 2025
pip install streamlit
Para ejecutar dese la línea de comando en cmd capeta donde este el archivo streamlit run "Arte Tokerizado2.py"
@author: alema
"""

import uuid
from datetime import datetime
import streamlit as st
import pickle
import os

# Ruta donde se guardarán los NFTs persistentes
DATA_FILE = "nft_data.pkl"

# Clase NFT para obras de arte
class ArtworkNFT:
    def __init__(self, title, artist, creation_date, owner, image_bytes=None, audio_bytes=None):
        self.token_id = str(uuid.uuid4())
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.metadata = {
            'resolution': '300dpi',
            'format': 'JPEG',
            'created': datetime.now().isoformat()
        }
        self.owner = owner
        self.image_bytes = image_bytes
        self.audio_bytes = audio_bytes
        self.transaction_history = []

    def transfer(self, new_owner):
        self.transaction_history.append({
            'from': self.owner,
            'to': new_owner,
            'date': datetime.now().isoformat()
        })
        self.owner = new_owner

    def show_info(self):
        return {
            'Token ID': self.token_id,
            'Title': self.title,
            'Artist': self.artist,
            'Creation Date': self.creation_date,
            'Current Owner': self.owner,
            'Metadata': self.metadata,
            'Transaction History': self.transaction_history
        }

# Funciones para guardar y cargar NFTs
def save_nfts(nft_registry):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(nft_registry, f)

def load_nfts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    return {}

# Cargar NFTs desde archivo si es la primera vez
if 'nft_registry' not in st.session_state:
    st.session_state.nft_registry = load_nfts()

# Interfaz Streamlit
st.set_page_config(page_title="Tokenización de Obras de Arte", layout="centered")
st.title("🎨 Tokenización de Obras de Arte")

action = st.sidebar.selectbox("Acción", ["Crear NFT", "Ver NFTs", "Transferir NFT"])

# Crear NFT
if action == "Crear NFT":
    st.subheader("🆕 Crear nueva obra de arte tokenizada")
    title = st.text_input("Título de la obra")
    artist = st.text_input("Artista")
    creation_date = st.date_input("Fecha de creación")
    owner = st.text_input("Propietario inicial")

    image_file = st.file_uploader("Sube una imagen (JPG, PNG)", type=["jpg", "jpeg", "png"])
    audio_file = st.file_uploader("Sube un archivo de audio (MP3)", type=["mp3"])

    if st.button("Crear NFT"):
        image_bytes = image_file.read() if image_file else None
        audio_bytes = audio_file.read() if audio_file else None

        nft = ArtworkNFT(title, artist, creation_date.strftime("%Y-%m-%d"), owner, image_bytes, audio_bytes)
        st.session_state.nft_registry[nft.token_id] = nft
        save_nfts(st.session_state.nft_registry)

        st.success(f"✅ NFT creado con ID: {nft.token_id}")

# Ver NFTs
elif action == "Ver NFTs":
    st.subheader("📄 NFTs Registrados")
    if st.session_state.nft_registry:
        for token_id, nft in st.session_state.nft_registry.items():
            st.markdown("---")
            st.markdown(f"### 🎟️ Token ID: `{token_id}`")
            info = nft.show_info()
            st.markdown(f"**Título:** {info['Title']}")
            st.markdown(f"**Artista:** {info['Artist']}")
            st.markdown(f"**Fecha de creación:** {info['Creation Date']}")
            st.markdown(f"**Propietario actual:** {info['Current Owner']}")

            if nft.image_bytes:
                st.image(nft.image_bytes, caption="Imagen del NFT", use_container_width=True)

            if nft.audio_bytes:
                st.audio(nft.audio_bytes, format="audio/mp3")
    else:
        st.warning("No hay NFTs registrados aún.")

# Transferir NFT
elif action == "Transferir NFT":
    st.subheader("🔁 Transferir propiedad de NFT")
    if st.session_state.nft_registry:
        token_ids = list(st.session_state.nft_registry.keys())
        selected_id = st.selectbox("Selecciona un Token ID", token_ids)
        new_owner = st.text_input("Nuevo propietario")

        if st.button("Transferir"):
            nft = st.session_state.nft_registry[selected_id]
            nft.transfer(new_owner)
            save_nfts(st.session_state.nft_registry)
            st.success(f"✅ Transferencia realizada. Nuevo propietario: {nft.owner}")
    else:
        st.warning("No hay NFTs registrados aún.")
