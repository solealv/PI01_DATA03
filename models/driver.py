from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Text
from config.db import meta, engine

drivers = Table('driver', meta, Column('driverId', Integer, primary_key=True), 
                                Column('driverRef', String(100)),
                                Column('num', Integer),
                                Column('code', String(10)),
                                Column('name', String(100)),
                                Column('dob', Date),
                                Column('nationality', String(100)),
                                Column('url', Text))

meta.create_all(engine)