import React, { useState } from 'react';

export default function App() {
  const [transferData, setTransferData] = useState({
    src: 'CUENTA_X',
    dst: '',
    amount: 100
  });
  const [logs, setLogs] = useState([]);

  const handleChange = (e) => {
    setTransferData({ ...transferData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('http://localhost:8000/api/transfer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          src: transferData.src,
          dst: transferData.dst,
          amount: parseFloat(transferData.amount)
        })
      });
      
      const result = await response.json();
      
      setLogs(prevLogs => [result, ...prevLogs]);
    } catch (error) {
      console.error("Error al conectar con el servidor", error);
    }
  };
  return (
      <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto', fontFamily: 'system-ui' }}>
        <h2>Simulador Bancario - Análisis de Grafos</h2>
        <p>Nodos sospechosos pre-cargados: SUSP_001, SUSP_002, SUSP_003</p>

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <input
            type="text" name="src" placeholder="Cuenta Origen"
            value={transferData.src} onChange={handleChange} required
          />
          <input
            type="text" name="dst" placeholder="Cuenta Destino (Ej. SUSP_001)"
            value={transferData.dst} onChange={handleChange} required
          />
          <input
            type="number" name="amount" placeholder="Monto"
            value={transferData.amount} onChange={handleChange} required
          />
          <button type="submit" style={{ padding: '10px', background: '#0070f3', color: 'white', border: 'none' }}>
            Realizar Transferencia
          </button>
        </form>

        <div style={{ marginTop: '30px' }}>
          <h3>Historial y Alertas</h3>
          {logs.map((log, index) => (
            <div key={index} style={{
              padding: '15px',
              marginBottom: '10px',
              borderRadius: '5px',
              border: log.anomaly_detected ? '2px solid red' : '1px solid #ddd',
              backgroundColor: log.anomaly_detected ? '#ffebeb' : '#f9f9f9'
            }}>
              <strong>{log.src} ➔ {log.dst} (${log.amount})</strong>
              <br />
              <span style={{ color: log.anomaly_detected ? 'red' : 'green', fontWeight: 'bold' }}>
                {log.message}
              </span>
            </div>
          ))}
        </div>
      </div>
    );
  }