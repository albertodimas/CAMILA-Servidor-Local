"use client";
import React from 'react';

export default function Layout({ children }) {
  return (
    <main style={{ padding: '2rem' }}>
      <h1>Interfaz CAMILA</h1>
      {children}
    </main>
  );
}
