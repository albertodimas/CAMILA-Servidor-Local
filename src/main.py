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
    # --- Extracción de características con la red ETER ---
    # Convierte la pregunta en un vector numérico fijo que servirá
    # como representación para el agente de refuerzo.
    features = eter_network.encode(pregunta)

    # --- Cálculo del estado para el agente FinRL ---
    # Se emplea numpy para sumar las características y proyectar el
    # resultado al rango de estados definidos en la tabla Q.
    import numpy as np
    state = int(np.array(features).sum()) % finrl_agent.q_table.shape[0]

    # El agente decide la acción a tomar en función del estado calculado.
    decision = finrl_agent.decide(state)

    # --- Generación de la respuesta con LLaMA-3 ---
    # Se enriquece el prompt original con la decisión adaptativa para
    # proveer contexto adicional al modelo de lenguaje.
    prompt_final = f"{pregunta}\n\nDecisión adaptativa: {decision}"
    result = llm.create_completion(prompt=prompt_final, max_tokens=256)
    respuesta = result['choices'][0]['text'].strip()

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
