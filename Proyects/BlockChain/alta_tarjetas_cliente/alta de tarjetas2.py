# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 21:05:27 2025

@author: alema
"""

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["Token"]
cripto = db["cripto"]

# Simular saldo inicial para varios usuarios
cripto.insert_many([
    {"usuario": "Carlos", "tarjeta": "123456", "cantidad": 5.0, "timestamp": datetime.utcnow()},
    {"usuario": "Ana", "tarjeta": "654321", "cantidad": 8.5, "timestamp": datetime.utcnow()},
    {"usuario": "Luis", "tarjeta": "789123", "cantidad": 4.2, "timestamp": datetime.utcnow()},
])