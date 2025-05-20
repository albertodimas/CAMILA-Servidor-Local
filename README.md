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
