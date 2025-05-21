from contextlib import asynccontextmanager
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route
from llama_cpp import Llama
import uvicorn
from .memoria import guardar_info, recuperar_info
# Componentes inteligentes: red ETER y agente FinRL
from .ia import eter_network, finrl_agent

llm = None


@asynccontextmanager
async def lifespan(app: Starlette):
    """Carga el modelo LLaMA durante el ciclo de vida de la aplicación."""
    global llm
    # Ruta fija al modelo cuantizado LLaMA-3.2-3B Instruct
    llm = Llama(model_path="models/Llama-3.2-3B-Instruct-Q4_K_M.gguf")
    yield


async def home(request):
    return PlainTextResponse('CAMILA Servidor Local Activo ✅')


async def ia(request):
    data = await request.json()
    pregunta = data.get('pregunta')
    if not pregunta:
        return JSONResponse({'error': 'pregunta no proporcionada'}, status_code=400)
    # Extraer características usando ETER
    features = eter_network.encode(pregunta)  # vector numérico

    # Decisión adaptativa mediante agente FinRL
    import numpy as np  # uso de numpy para el cálculo
    state = int(np.array(features).sum()) % finrl_agent.q_table.shape[0]  # estado discreto
    decision = finrl_agent.decide(state)  # acción propuesta por el agente

    # Construir prompt enriquecido según decisión FinRL
    prompt_final = f"{pregunta}\n\nDecisión adaptativa: {decision}"  # prompt final

    # Finalmente, respuesta enriquecida mediante LLaMA-3
    result = llm.create_completion(prompt=prompt_final, max_tokens=256)  # generación con LLaMA
    respuesta = result['choices'][0]['text'].strip()  # extracción de texto

    return JSONResponse({'respuesta': respuesta})

async def memoria_guardar(request):
    data = await request.json()
    contenido = data.get('contenido')
    if not contenido:
        return JSONResponse({'error': 'contenido no proporcionado'}, status_code=400)
    guardar_info(contenido)
    return JSONResponse({'status': 'guardado'})

async def memoria_recuperar(request):
    docs = recuperar_info()
    textos = [doc.page_content for doc in docs]
    return JSONResponse({'memoria': textos})


async def status(request):
    return JSONResponse({"status": "CAMILA operativo ✅"})

routes = [
    Route('/', home, methods=["GET"]),
    Route('/ia', ia, methods=["POST"]),
    Route('/memoria/guardar', memoria_guardar, methods=["POST"]),
    Route('/memoria/recuperar', memoria_recuperar, methods=["GET"]),
]

routes.append(Route('/status', status, methods=["GET"]))

app = Starlette(routes=routes, lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
