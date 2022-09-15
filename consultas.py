import requests
import pandas as pd

def get_datos(datos):
    url = 'http://localhost:8000/' + datos
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    return df

# Obtencion de las tabas para realizar las consultas
# Las guardo como variables globales 
circuit = get_datos('circuit')
constructor = get_datos('constructor')
driver = get_datos('driver')
pit_stop = get_datos('pit_stop')
race = get_datos('race')
result = get_datos('result')

# Año con más carreras
def anioMasCarreras():
    agrupados = race.groupby(['year']).count()
    max = agrupados.raceId.max()
    anio_max = agrupados.raceId.idxmax()

    return print(f'Consulta 1: \nEl año con más carreras fue {anio_max} con {max} carreras en total\n')
anioMasCarreras()

# Piloto con mayor cantidad de primeros puestos
def pilotoPrimerPuesto():
    # Armo una tabla que contenga los nombres de los pilotos con las posiciones que obtuvieron en cada carrera
    # Para esto uno las tablas `result` y `driver` sobre la columna driverId. 
    # Filtro por las columnas sobre las que voy a trabajar.
    resultados_totales = pd.merge(result, driver, how='left', on='driverId')[['resultId','position', 'name']]

    # Ahora sobre la tabla resultante, filtro los registros cuyos valores en posicion sean 1
    # de esta manera obtengo una lista solo con los primeros puestos. 
    # A su vez, agrupo por el nombre de los pilotos y cuento los resultados.

    # Con idxmax() obtengo el nombre del piloto, ya que al agrupar el indice pasa a ser el nombre del piloto.
    nombre = resultados_totales[resultados_totales.position==1].groupby('name').count()['position'].idxmax()
    
    # Con max() obtengo el numero de titulos obtenidos por el piloto
    titulos = resultados_totales[resultados_totales.position==1].groupby('name').count()['position'].max()
    
    return print(f'Consulta 2: \nEl piloto con mayor cantidad de titulos es {nombre} con {titulos} titulos en total.\n')
pilotoPrimerPuesto()

# Nombre del circuito más corrido
def circuitoMax():
    circuitos_id = pd.merge(result, race, how='left', on='raceId')[['raceId', 'circuitId']]
    circuitos_nombre = pd.merge(circuitos_id, circuit, how='left', on='circuitId')[['raceId', 'name']]
    circuitos_nombre.drop_duplicates(inplace=True)
    num_carreras = circuitos_nombre.groupby('name').count()['raceId'].max()
    circuito = circuitos_nombre.groupby('name').count()['raceId'].idxmax()
    return print(f'Consulta 3: \nEl circuito mas corrido es {circuito} con un total de {num_carreras} carreras realizadas.\n')
circuitoMax()

# Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
def pilotoMax():
    constructores = pd.merge(result, constructor, how='left', on='constructorId')[['driverId', 'constructorId','points','name', 'nationality']]
    BriAm = constructores[constructores.nationality.isin(['British', 'American'])]
    BriAm2 = pd.merge(BriAm, driver, how='left', on='driverId')[['name_y', 'name_x', 'nationality_x', 'points']]
    BriAm2.rename(columns = {'name_y':'driver_name', 'name_x':'constructor_name', 'nationality_x':'constructor_nationality'}, inplace = True)
    suma_puntos= BriAm2.groupby(by=['driver_name', 'constructor_nationality']).sum()
    suma_puntos.reset_index(inplace=True)
    suma_puntos.set_index('driver_name', inplace=True)
    nom_Bri = suma_puntos[suma_puntos.constructor_nationality == 'British']['points'].idxmax()
    p_Bri = suma_puntos[suma_puntos.constructor_nationality == 'British']['points'].max()
    nom_Am = suma_puntos[suma_puntos.constructor_nationality == 'American']['points'].idxmax()
    p_Am = suma_puntos[suma_puntos.constructor_nationality == 'American']['points'].max()
    return print(f'Consulta 4: \nEl piloto que gano mas puntos con un constructor americano fue {nom_Am}, sumando un total de {p_Am} puntos. \nEl piloto que gano mas puntos con un constructor britanico fue {nom_Bri}, sumando un total de {p_Bri} puntos.\n')
pilotoMax()