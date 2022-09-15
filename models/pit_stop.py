from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Time, Numeric
from config.db import meta, engine

pit_stops = Table('pit_stop', meta, Column('raceId', Integer, primary_key=True), 
                                Column('driverId', Integer),
                                Column('stop', Integer),
                                Column('lap', Integer),
                                Column('time', String(15)),
                                Column('duration', Numeric(5,3)),
                                Column('milliseconds', Integer))

meta.create_all(engine)