"use client";
import React, { useState } from 'react';
import { CopilotProvider } from '@copilotkit/react-core';
// Importamos los componentes de manera explícita con la extensión
// para evitar resolver rutas incorrectas en ciertos entornos de build.
import Layout from '../components/Layout';
import AskSection from '../components/AskSection';
import MemorySection from '../components/MemorySection';

export default function Home() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [memory, setMemory] = useState('');
  const [memData, setMemData] = useState([]);

  const ask = async () => {
    const res = await fetch('http://localhost:8000/ia', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pregunta: question })
    });
    const data = await res.json();
    setAnswer(data.respuesta);
  };

  const saveMemory = async () => {
    await fetch('http://localhost:8000/memoria/guardar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ contenido: memory })
    });
    setMemory('');
  };

  const getMemory = async () => {
    const res = await fetch('http://localhost:8000/memoria/recuperar');
    const data = await res.json();
    setMemData(data.memoria);
  };

  return (
    <CopilotProvider>
      <Layout>
        <AskSection
          question={question}
          onQuestionChange={setQuestion}
          onSend={ask}
          answer={answer}
        />
        <MemorySection
          memory={memory}
          onMemoryChange={setMemory}
          onSave={saveMemory}
          onRetrieve={getMemory}
          data={memData}
        />
      </Layout>
    </CopilotProvider>
  );
}
