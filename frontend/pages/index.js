import { useState } from 'react';
import { CopilotProvider } from '@copilotkit/react-core';

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
      <main style={{ padding: '2rem' }}>
        <h1>Interfaz CAMILA</h1>

        <section>
          <h2>Consultar IA</h2>
          <input
            aria-label="pregunta"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button onClick={ask}>Enviar</button>
          <div>Respuesta: {answer}</div>
        </section>

        <section>
          <h2>Memoria Persistente</h2>
          <input
            aria-label="memoria"
            value={memory}
            onChange={(e) => setMemory(e.target.value)}
          />
          <button onClick={saveMemory}>Guardar</button>
          <button onClick={getMemory}>Recuperar</button>
          <ul>
            {memData.map((text, i) => (
              <li key={i}>{text}</li>
            ))}
          </ul>
        </section>
      </main>
    </CopilotProvider>
  );
}
