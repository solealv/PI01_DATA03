from config.db import engine
import pandas as pd

# Creacion de los Dataframes a partir de los datasets provistos

circuit = pd.DataFrame(pd.read_csv('.models/Datasets/circuits.csv'))
circuit

constructor = pd.DataFrame(pd.read_json('./Datasets/constructors.json', lines=True))
constructor

driver = pd.DataFrame(pd.read_json('./Datasets/drivers.json', lines=True))
name = pd.DataFrame(list(driver['name'].values))
driver['name'] = name.forename + ' ' + name.surname
driver

pit_stop= pd.DataFrame(pd.read_json('./Datasets/pit_stops.json'))
pit_stop

result = pd.DataFrame(pd.read_json('./Datasets/results.json', lines=True))
result

race = pd.DataFrame(pd.read_csv('./Datasets/races.csv'))
race

# Creacion de tablas en MySQL y carga de datos a partir de los DF creados con los dataset

circuits = circuit.to_sql(con = engine, name='circuit', if_exists='replace', index=False)
constructor.to_sql(con = engine, name='constructor', if_exists='replace', index=False)
driver.to_sql(con = engine, name='driver', if_exists='replace', index=False)
pit_stop.to_sql(con = engine, name='pit_stop', if_exists='replace', index=False)
race.to_sql(con = engine, name='race', if_exists='replace', index=False)
result.to_sql(con = engine, name='result', if_exists='replace', index=False)

 
