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

4. **Ejecutar el servidor local**

```bash
python main.py
```

Accede a [http://localhost:8000](http://localhost:8000) para comprobar que el servidor responde con:

```
CAMILA Servidor Local Activo ✅
```

5. **Descargar el modelo LLaMA-3.2-3b cuantizado**

Descarga el modelo `gguf` de LLaMA y ubícalo en la carpeta `models/`. Define la
variable de entorno `LLAMA_MODEL_PATH` con la ruta al archivo, por ejemplo:

```bash
export LLAMA_MODEL_PATH=./models/llama-3.2-3b-q4.gguf
```

6. **Probar el endpoint de IA**

Con el servidor en marcha envía una petición POST a `/ia`:

```bash
curl -X POST http://localhost:8000/ia \
     -H 'Content-Type: application/json' \
     -d '{"pregunta": "¿Hola?"}'
```

La respuesta incluirá una clave `respuesta` generada por el modelo.

7. **Usar la memoria persistente**

Para guardar información contextual envía una petición POST a `/memoria/guardar`:

```bash
curl -X POST http://localhost:8000/memoria/guardar \
     -H 'Content-Type: application/json' \
     -d '{"contenido": "mi texto"}'
```

Recupera todo lo almacenado con una petición GET a `/memoria/recuperar`:

```bash
curl http://localhost:8000/memoria/recuperar
```

La respuesta contendrá una lista `memoria` con los textos guardados.
8. **Ejecutar las pruebas automáticas**

```bash
pytest
```
