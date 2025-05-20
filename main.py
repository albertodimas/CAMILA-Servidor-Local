from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
import uvicorn

app = Starlette()

@app.route('/')
async def read_root(request):
    return PlainTextResponse('CAMILA Servidor Local Activo ✅')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
