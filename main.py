from fastapi import FastAPI
from routes.circuitos import circuit



app = FastAPI()

app.include_router(circuit)

@app.get('/')
def helloworld():
    return 'Hello world'