import os
from contextlib import asynccontextmanager
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route
from llama_cpp import Llama
import uvicorn

from .memoria import guardar_info, recuperar_info

llm = None

@asynccontextmanager
async def lifespan(app: Starlette):
    """Load the LLaMA model when the app starts."""
    global llm
    model_path = os.getenv("LLAMA_MODEL_PATH", "models/Llama-3.2-3B-Instruct-Q4_K_M.gguf")
    llm = Llama(model_path=model_path)
    yield


async def home(request):
    return PlainTextResponse("CAMILA Servidor Local Activo ✅")


async def status(request):
    return JSONResponse({"status": "CAMILA operativo ✅"})


async def ia(request):
    data = await request.json()
    pregunta = data.get("pregunta")
    if not pregunta:
        return JSONResponse({"error": "pregunta no proporcionada"}, status_code=400)
    result = llm.create_completion(prompt=pregunta, max_tokens=128)
    respuesta = result["choices"][0]["text"].strip()
    return JSONResponse({"respuesta": respuesta})


async def memoria_guardar(request):
    data = await request.json()
    contenido = data.get("contenido")
    if not contenido:
        return JSONResponse({"error": "contenido no proporcionado"}, status_code=400)
    guardar_info(contenido)
    return JSONResponse({"status": "guardado"})


async def memoria_recuperar(request):
    docs = recuperar_info()
    textos = [doc.page_content for doc in docs]
    return JSONResponse({"memoria": textos})


routes = [
    Route("/", home, methods=["GET"]),
    Route("/status", status, methods=["GET"]),
    Route("/ia", ia, methods=["POST"]),
    Route("/memoria/guardar", memoria_guardar, methods=["POST"]),
    Route("/memoria/recuperar", memoria_recuperar, methods=["GET"]),
]

app = Starlette(routes=routes, lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
