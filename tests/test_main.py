from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert 'CAMILA Servidor Local Activo' in response.text


def test_ia_endpoint():
    response = client.post('/ia', json={'pregunta': 'Hola?'})
    assert response.status_code == 200
    data = response.json()
    assert 'respuesta' in data
