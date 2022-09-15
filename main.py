from fastapi import FastAPI
from routes.circuit import circuit
from routes.constructor import cons
from routes.driver import driver
from routes.pit_stop import pit_stop
from routes.race import race
from routes.result import result


app = FastAPI(title='Datasets Formula 1',
              description='Esta API contiene datos sobre la Formula 1')

app.include_router(circuit)
app.include_router(cons)
app.include_router(driver)
app.include_router(pit_stop)
app.include_router(race)
app.include_router(result)

@app.get('/')
def inicio():
    return 'Ingrese a localhost:8000/docs para mas informacion sobre el contenido de esta API'