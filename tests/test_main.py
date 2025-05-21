import os
from src import main
from starlette.testclient import TestClient

class DummyLlama:
    """Captures the prompt used to generate the completion."""
    def __init__(self):
        self.last_prompt = None

    def create_completion(self, prompt, max_tokens=128):
        self.last_prompt = prompt
        return {"choices": [{"text": "respuesta de prueba"}]}

class DummyETER:
    def encode(self, text):
        return [0] * 16
    def forward(self, x):
        return [0, 0]

import numpy as np

class DummyFinRL:
    def __init__(self):
        # q_table con atributo shape simulado
        self.q_table = np.array([[0, 0]] * 10)

    def decide(self, state):
        return 0

def test_ia_endpoint(monkeypatch):
    dummy_llama = DummyLlama()
    monkeypatch.setattr(main, "Llama", lambda model_path: dummy_llama)
    monkeypatch.setenv("LLAMA_MODEL_PATH", "dummy")
    monkeypatch.setattr(main, "eter_network", DummyETER())
    monkeypatch.setattr(main, "finrl_agent", DummyFinRL())

    with TestClient(main.app) as client:
        response = client.post("/ia", json={"pregunta": "Hola?"})
        assert response.status_code == 200
        assert response.json()["respuesta"] == "respuesta de prueba"
        # Verifica que el prompt incluya la decisión adaptativa
        assert "Decisión adaptativa: 0" in dummy_llama.last_prompt


def test_status_endpoint():
    from starlette.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {"status": "CAMILA operativo ✅"}

