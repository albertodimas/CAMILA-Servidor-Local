export default function AskSection({ question, onQuestionChange, onSend, answer }) {
  return (
    <section>
      <h2>Consultar IA</h2>
      <input
        aria-label="pregunta"
        value={question}
        onChange={(e) => onQuestionChange(e.target.value)}
      />
      <button onClick={onSend}>Enviar</button>
      <div>Respuesta: {answer}</div>
    </section>
  );
}
