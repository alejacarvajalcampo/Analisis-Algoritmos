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
  }; }