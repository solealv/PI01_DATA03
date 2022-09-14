from copyreg import constructor
from fastapi import FastAPI
from routes.circuitos import circuit
from routes.constructor import cons
from routes.driver import driver
from routes.pit_stop import pit_stop
from routes.race import race
from routes.result import result


app = FastAPI()

app.include_router(circuit)
app.include_router(cons)
app.include_router(driver)
app.include_router(pit_stop)
app.include_router(race)
app.include_router(result)

@app.get('/')
def helloworld():
    return 'Hello world'