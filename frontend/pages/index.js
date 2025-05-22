import React, { useState } from 'react';
import Layout from '../components/Layout.js';
import AskSection from '../components/AskSection.js';
import MemorySection from '../components/MemorySection.js';

export default function Home() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [memory, setMemory] = useState('');
  const [memData, setMemData] = useState([]);

  return (
    <Layout>
      <AskSection 
        question={question}
        onQuestionChange={setQuestion}
        onSend={() => {}}
        answer={answer}
      />
      <MemorySection 
        memory={memory}
        onMemoryChange={setMemory}
        onSave={() => {}}
        onRetrieve={() => {}}
        data={memData}
      />
    </Layout>
  );
}
