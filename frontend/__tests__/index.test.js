import { render, screen, fireEvent } from '@testing-library/react';
import Home from '../pages/index';

global.fetch = jest.fn(() => Promise.resolve({
  json: () => Promise.resolve({ respuesta: 'ok', memoria: ['a'] })
}));

test('realiza consulta IA', async () => {
  render(<Home />);
  fireEvent.change(screen.getByLabelText('pregunta'), { target: { value: 'hola' } });
  fireEvent.click(screen.getByText('Enviar'));
  expect(fetch).toHaveBeenCalledWith('http://localhost:8000/ia', expect.any(Object));
});

test('guarda en memoria', async () => {
  render(<Home />);
  fireEvent.change(screen.getByLabelText('memoria'), { target: { value: 'dato' } });
  fireEvent.click(screen.getByText('Guardar'));
  expect(fetch).toHaveBeenCalledWith('http://localhost:8000/memoria/guardar', expect.any(Object));
});
