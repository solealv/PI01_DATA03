from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

constructors = Table('constructor', meta, Column('constructorId', Integer, primary_key=True), 
                                Column('constructorRef', String(255)),
                                Column('name', String(255)),
                                Column('nationality', String(255)))


meta.create_all(engine)