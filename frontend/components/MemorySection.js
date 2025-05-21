"use client";
import React from 'react';

export default function MemorySection({ memory, onMemoryChange, onSave, onRetrieve, data }) {
  return (
    <section>
      <h2>Memoria Persistente</h2>
      <input
        aria-label="memoria"
        value={memory}
        onChange={(e) => onMemoryChange(e.target.value)}
      />
      <button onClick={onSave}>Guardar</button>
      <button onClick={onRetrieve}>Recuperar</button>
      <ul>
        {data.map((text, i) => (
          <li key={i}>{text}</li>
        ))}
      </ul>
    </section>
  );
}
