import os
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from llama_cpp import Llama
import uvicorn
from memoria import guardar_info, recuperar_info

app = Starlette()

llm = None

@app.on_event("startup")
async def load_model():
    """Carga el modelo LLaMA al iniciar la aplicación."""
    global llm
    # Ruta fija al modelo cuantizado LLaMA-3.2-3B Instruct
    llm = Llama(model_path="models/Llama-3.2-3B-Instruct-Q4_K_M.gguf")

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


@app.route('/memoria/guardar', methods=['POST'])
async def memoria_guardar(request):
    data = await request.json()
    contenido = data.get('contenido')
    if not contenido:
        return JSONResponse({'error': 'contenido no proporcionado'}, status_code=400)
    guardar_info(contenido)
    return JSONResponse({'status': 'guardado'})


@app.route('/memoria/recuperar', methods=['GET'])
async def memoria_recuperar(request):
    docs = recuperar_info()
    textos = [doc.page_content for doc in docs]
    return JSONResponse({'memoria': textos})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
