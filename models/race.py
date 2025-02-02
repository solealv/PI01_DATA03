from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text, Date, Time
from config.db import meta, engine

races = Table('race', meta, Column('raceId', Integer, primary_key=True), 
                                Column('year', Integer),
                                Column('round', Integer),
                                Column('circuitId', Integer),
                                Column('name', String(100)),
                                Column('date', String(15)),
                                Column('time', String(15)),
                                Column('url', Text))

meta.create_all(engine)