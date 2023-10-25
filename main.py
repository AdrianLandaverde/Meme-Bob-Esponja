from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world(frase: str):
    return {'message':'Hello World'}

@app.get("/{frase}")
def burla(frase: str):
    for vocal in 'aeiouAEIOU':
        frase = frase.replace(vocal, 'i')
    return {'message':frase}
