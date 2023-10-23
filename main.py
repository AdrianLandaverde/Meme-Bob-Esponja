from fastapi import FastAPI

app = FastAPI()

@app.get("/{frase}")
def hello_world(frase: str):
    for vocal in 'aeiouAEIOU':
        frase = frase.replace(vocal, 'i')
    return frase