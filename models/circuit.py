from cgi import parse_multipart
from sqlite3 import IntegrityError
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import meta, engine

circuits = Table('circuit', meta, Column('circuitId', Integer, primary_key=True), 
                                Column('circuitRef', String(100)),
                                Column('name', String(100)),
                                Column('location', String(100)),
                                Column('country', String(100)),
                                Column('lat', Numeric(9,5)),
                                Column('lng', Numeric(9,5)),
                                Column('alt', Numeric(9,5)),
                                Column('url', String(100)))


meta.create_all(engine)