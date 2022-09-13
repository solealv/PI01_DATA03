from cgi import parse_multipart
from sqlite3 import IntegrityError
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

circuits = Table('circuit', meta, Column('circuitId', Integer, primary_key=True), 
                                Column('circuitRef', String(255)),
                                Column('name', String(255)),
                                Column('location', String(255)),
                                Column('country', String(255)),
                                Column('lat', String(255)),
                                Column('lng', String(255)),
                                Column('alt', String(255)),
                                Column('url', String(255)))


meta.create_all(engine)