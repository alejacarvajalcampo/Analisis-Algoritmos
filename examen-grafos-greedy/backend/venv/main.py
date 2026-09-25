from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
from collections import defaultdict
from typing import List, Dict, Set

# Inicializar aplicación
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELO DE GRAFOS ---
class Account:
    def __init__(self, account_id: str, is_suspicious: bool = False):
        self.account_id = account_id
        self.is_suspicious = is_suspicious

class Transaction:
    def __init__(self, src: str, dst: str, amount: float, timestamp: float):
        self.src = src
        self.dst = dst
        self.amount = amount
        self.timestamp = timestamp

class BankGraphModel:
    # AUMENTÉ LA VENTANA A 60 SEGUNDOS para que tengas tiempo de sobra
    def __init__(self, time_window_seconds: int = 60, suspicious_threshold: int = 3):
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
        
        # Filtra destinos únicos sospechosos
        suspicious_destinations = {
            t.dst for t in recent_transactions if self.accounts[t.dst].is_suspicious
        }
        
        # LOGS EN CONSOLA: Esto te mostrará qué está pensando el backend
        print(f"\n--- Analizando nodo origen: {src_account_id} ---")
        print(f"Destinos maliciosos únicos contactados: {suspicious_destinations}")
        print(f"Total conectados: {len(suspicious_destinations)} / {self.suspicious_threshold} requeridos para alerta")
        
        return len(suspicious_destinations) >= self.suspicious_threshold

# Instancia global del grafo
graph_model = BankGraphModel(time_window_seconds=60, suspicious_threshold=3)

# Cargar nodos sospechosos iniciales
for acc in ["SUSP_001", "SUSP_002", "SUSP_003", "SUSP_004"]:
    graph_model.add_account(acc, is_suspicious=True)

# --- CONTROLADOR / ENDPOINTS ---
class TransferRequest(BaseModel):
    src: str
    dst: str
    amount: float

@app.post("/api/transfer")
def process_transfer(req: TransferRequest):
    current_time = time.time()
    
    # CORRECCIÓN DE ERRORES HUMANOS: Quita espacios y fuerza a mayúsculas
    src_clean = req.src.strip().upper()
    dst_clean = req.dst.strip().upper()
    
    # Se evalúa el grafo
    is_anomalous = graph_model.add_transaction(src_clean, dst_clean, req.amount, current_time)
    
    return {
        "src": src_clean,
        "dst": dst_clean,
        "amount": req.amount,
        "anomaly_detected": is_anomalous,
        "message": "ALERTA DE FRAUDE: Patrón de grafo anómalo" if is_anomalous else "Transferencia exitosa"
    }