from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

drivers = Table('driver', meta, Column('driverId', Integer, primary_key=True), 
                                Column('driverRef', String(255)),
                                Column('number', String(255)),
                                Column('code', String(255)),
                                Column('name', String(255)),
                                Column('dob', String(255)),
                                Column('nationality', String(255)),
                                Column('url', String(255)))

meta.create_all(engine)