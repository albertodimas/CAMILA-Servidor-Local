import os
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from llama_cpp import Llama
import uvicorn

app = Starlette()

llm = None

@app.on_event("startup")
async def load_model():
    """Carga el modelo LLaMA al iniciar la aplicación."""
    global llm
    model_path = os.getenv("LLAMA_MODEL_PATH", "model.gguf")
    llm = Llama(model_path=model_path)

@app.route('/')
async def read_root(request):
    return PlainTextResponse('CAMILA Servidor Local Activo ✅')


@app.route('/ia', methods=['POST'])
async def ia(request):
    data = await request.json()
    pregunta = data.get('pregunta')
    if not pregunta:
        return JSONResponse({'error': 'pregunta no proporcionada'}, status_code=400)
    result = llm.create_completion(prompt=pregunta, max_tokens=128)
    respuesta = result['choices'][0]['text'].strip()
    return JSONResponse({'respuesta': respuesta})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
