from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

pit_stops = Table('pit_stop', meta, Column('raceId', Integer, primary_key=True), 
                                Column('driverId', String(255)),
                                Column('stop', String(255)),
                                Column('lap', String(255)),
                                Column('time', String(255)),
                                Column('duration', String(255)),
                                Column('milliseconds', String(255)))

meta.create_all(engine)