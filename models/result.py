from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric, Text
from config.db import meta, engine

results = Table('result', meta, Column('resultId', Integer, primary_key=True), 
                                Column('raceId', Integer),
                                Column('driverId', Integer),
                                Column('constructorId', Integer),
                                Column('number', String(10)),
                                Column('grid', Integer),
                                Column('position', Integer),
                                Column('positionText', String(10)),
                                Column('positionOrder', Integer),
                                Column('points', Numeric(6,2)),
                                Column('laps', Integer),
                                Column('time', Text),
                                Column('milliseconds', Text),
                                Column('fastestLap', Text),
                                Column('rank', Text),
                                Column('fastestLapTime', Text),
                                Column('fastestLapSpeed', Text),
                                Column('statusId', Integer))

meta.create_all(engine)