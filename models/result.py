from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

results = Table('result', meta, Column('resultId', Integer, primary_key=True), 
                                Column('raceId', String(255)),
                                Column('driverId', String(255)),
                                Column('constructorId', String(255)),
                                Column('number', String(255)),
                                Column('grid', String(255)),
                                Column('position', String(255)),
                                Column('positionText', String(255)),
                                Column('positionOrder', String(255)),
                                Column('points', String(255)),
                                Column('laps', String(255)),
                                Column('time', String(255)),
                                Column('milliseconds', String(255)),
                                Column('fastestLap', String(255)),
                                Column('rank', String(255)),
                                Column('fastestLapTime', String(255)),
                                Column('fastestLapSpeed', String(255)),
                                Column('StatusId', String(255)))


meta.create_all(engine)