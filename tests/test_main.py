import os
from src import main
from starlette.testclient import TestClient

class DummyLlama:
    def create_completion(self, prompt, max_tokens=128):
        return {"choices": [{"text": "respuesta de prueba"}]}

def test_ia_endpoint(monkeypatch):
    monkeypatch.setattr(main, "Llama", lambda model_path: DummyLlama())
    monkeypatch.setenv("LLAMA_MODEL_PATH", "dummy")
    with TestClient(main.app) as client:
        response = client.post("/ia", json={"pregunta": "Hola?"})
        assert response.status_code == 200
        assert response.json()["respuesta"] == "respuesta de prueba"


def test_status_endpoint():
    from starlette.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {"status": "CAMILA operativo ✅"}
