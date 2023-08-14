import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hola, soy vuestro profesor de Ciencia de Datos"}


@app.get('/{name}')
def get_name(name: str):
    return {"message": f"Me llamo {name} y espero que os guste este tutorial"}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
