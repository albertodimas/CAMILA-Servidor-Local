import types
from src import memoria
from src.memoria import guardar_info, recuperar_info

class DummyCollection:
    def __init__(self):
        self.docs = []
    def add(self, documents, ids):
        self.docs.extend(documents)
    def get(self, include=None):
        return {"documents": self.docs}

class DummyClient:
    def __init__(self, path=None):
        self.collection = DummyCollection()
    def get_or_create_collection(self, name):
        return self.collection

def test_memoria(monkeypatch):
    dummy_chroma = types.SimpleNamespace(PersistentClient=DummyClient)
    monkeypatch.setattr(memoria, "chromadb", dummy_chroma)
    memoria._client = None
    memoria._collection = None

    guardar_info("dato")
    docs = recuperar_info()
    assert docs[0].page_content == "dato"
