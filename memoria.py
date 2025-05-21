import uuid
import chromadb
from langchain.schema import Document

_client = None
_collection = None


def init_memoria(persist_directory: str = "memoria_db"):
    """Inicializa el cliente y la colección de ChromaDB."""
    global _client, _collection
    if _client is None:
        _client = chromadb.PersistentClient(path=persist_directory)
        _collection = _client.get_or_create_collection("memoria")


def guardar_info(contenido: str) -> None:
    """Guarda un texto en la base de memoria persistente."""
    init_memoria()
    _collection.add(documents=[contenido], ids=[str(uuid.uuid4())])


def recuperar_info() -> list[Document]:
    """Recupera todos los documentos almacenados."""
    init_memoria()
    result = _collection.get(include=["documents"])
    return [Document(page_content=doc) for doc in result.get("documents", [])]
