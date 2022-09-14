from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

races = Table('race', meta, Column('raceId', Integer, primary_key=True), 
                                Column('year', String(255)),
                                Column('round', String(255)),
                                Column('circuitId', String(255)),
                                Column('name', String(255)),
                                Column('date', String(255)),
                                Column('time', String(255)),
                                Column('url', String(255)))


meta.create_all(engine)