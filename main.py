import os
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.requests import Request
import uvicorn

try:
    from llama_cpp import Llama
except ImportError:  # fallback stub for environments without llama-cpp-python
    Llama = None

MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "models/llama-3.2-3b.gguf")

app = Starlette()

_llm = None

def get_llm():
    global _llm
    if _llm is None and Llama is not None:
        _llm = Llama(model_path=MODEL_PATH)
    return _llm

@app.route('/')
async def read_root(request):
    return PlainTextResponse('CAMILA Servidor Local Activo ✅')


@app.route('/ia', methods=['POST'])
async def ask_ia(request: Request):
    data = await request.json()
    pregunta = data.get('pregunta', '')
    llm = get_llm()
    if llm is None:
        respuesta = 'Modelo no disponible'
    else:
        output = llm(pregunta, max_tokens=128)
        respuesta = output["choices"][0]["text"].strip()
    return JSONResponse({"respuesta": respuesta})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
