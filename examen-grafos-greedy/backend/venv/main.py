from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
from collections import defaultdict
from typing import List, Dict, Set

# Inicializar aplicación
app = FastAPI()

# Permitir conexiones desde el frontend en React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELO DE GRAFOS ---
class Account:
    def _init_(self, account_id: str, is_suspicious: bool = False):
        self.account_id = account_id
        self.is_suspicious = is_suspicious

class Transaction:
    def _init_(self, src: str, dst: str, amount: float, timestamp: float):
        self.src = src
        self.dst = dst
        self.amount = amount
        self.timestamp = timestamp