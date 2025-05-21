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

5. **Descargar el modelo LLaMA-3.2-3B Instruct cuantizado**

Descarga manualmente el archivo `Llama-3.2-3B-Instruct-Q4_K_M.gguf` desde
[Hugging Face](https://huggingface.co/).  Una vez descargado, colócalo en la
carpeta `models` incluida en este proyecto.  El servidor buscará el modelo en
`models/Llama-3.2-3B-Instruct-Q4_K_M.gguf` al iniciar.

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

9. **Ejecutar la interfaz visual**

La interfaz React basada en Next.js se encuentra en `frontend` y utiliza CopilotKit para facilitar la interacción.

```bash
cd frontend
npm install
npm run dev
```

Esto abrirá la web en [http://localhost:3000](http://localhost:3000). Desde ella podrás consultar el endpoint `/ia` y gestionar la memoria con `/memoria/guardar` y `/memoria/recuperar`.

Para ejecutar las pruebas de la interfaz:

```bash
npm test
```

## Estructura avanzada del frontend

El directorio `frontend` contiene una aplicación basada en React, Next.js y CopilotKit.
La estructura inicial está organizada para facilitar la extensión:

```
frontend/
  components/        # Componentes reutilizables de la interfaz
    AskSection.js
    MemorySection.js
    Layout.js
  pages/             # Páginas Next.js
    index.js
  __tests__/         # Pruebas con Jest y Testing Library
    index.test.js
  jest.config.js     # Configuración de Jest
  package.json       # Scripts y dependencias
```

### Scripts disponibles

Desde `frontend` se puede iniciar el servidor de desarrollo con:

```bash
npm run dev
```

Y ejecutar las pruebas automáticas con:

```bash
npm test
```

