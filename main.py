from fastapi import FastAPI
import vertexai
from vertexai.language_models import TextGenerationModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {'message':'Hello World'}

@app.get("/gcloud")
def hello_world():
    vertexai.init(project="hip-principle-403314", location="us-central1")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(
        """What are the advantages of using google cloud for AI models""",
        **parameters
    )
    print(f"Response from Model: {response.text}")
    return {'message':'Hello World'}

@app.get("/{frase}")
def burla(frase: str):
    for vocal in 'aeiouAEIOU':
        frase = frase.replace(vocal, 'i')
    return {'message':frase}
