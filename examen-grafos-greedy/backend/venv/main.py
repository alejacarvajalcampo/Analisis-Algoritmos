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

class BankGraphModel:
    def _init_(self, time_window_seconds: int = 10, suspicious_threshold: int = 3):
        self.accounts: Dict[str, Account] = {}
        self.graph: Dict[str, List[Transaction]] = defaultdict(list)
        self.time_window = time_window_seconds
        self.suspicious_threshold = suspicious_threshold

    def add_account(self, account_id: str, is_suspicious: bool = False):
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id, is_suspicious)

    def add_transaction(self, src: str, dst: str, amount: float, timestamp: float) -> bool:
        self.add_account(src)
        self.add_account(dst)

        transaction = Transaction(src, dst, amount, timestamp)
        self.graph[src].append(transaction)

        return self._detect_anomaly(src, timestamp)

    def _detect_anomaly(self, src_account_id: str, current_time: float) -> bool:
        recent_transactions = [
            t for t in self.graph[src_account_id]
            if current_time - t.timestamp <= self.time_window
        ]
        suspicious_destinations = {
            t.dst for t in recent_transactions if self.accounts[t.dst].is_suspicious
        }
        return len(suspicious_destinations) >= self.suspicious_threshold