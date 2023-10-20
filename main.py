from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

#devuelve una pagina web
@app.get("/",response_class=JSONResponse)
def hola():
    return {"Hola!"}
