# CAMILA-Servidor-Local
Servidor local básico con Starlette y Uvicorn, optimizado para ejecutar el modelo LLaMA-3.2-3b (llama.cpp) del proyecto CAMILA.

## Instrucciones

1. **Clonar el repositorio**

```bash
git clone <URL-del-repositorio>
cd CAMILA-Servidor-Local
```

2. **Crear y activar un entorno virtual de Python 3.11**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instalar las dependencias**

```bash
pip install -r requirements.txt
```

4. **Descargar el modelo LLaMA-3.2-3b cuantizado**

   Descarga el modelo `llama-3.2-3b.gguf` y colócalo en la carpeta `models/`.
   También puedes especificar la ruta exportando la variable
   `LLAMA_MODEL_PATH`.

5. **Ejecutar el servidor local**

```bash
python main.py
```

Accede a [http://localhost:8000](http://localhost:8000) para comprobar que el servidor responde con:

```
CAMILA Servidor Local Activo ✅
```

Para consultar el modelo usa el endpoint `/ia`:

```bash
curl -X POST http://localhost:8000/ia -H 'Content-Type: application/json' \
     -d '{"pregunta": "¿Cuál es tu nombre?"}'
```
