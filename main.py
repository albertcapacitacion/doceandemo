from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()

#devuelve una pagina web
@app.get("/")
async def read_root():
    return FileResponse('index.html')
