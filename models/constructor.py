from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

constructors = Table('constructor', meta, Column('constructorId', Integer, primary_key=True), 
                                Column('constructorRef', String(100)),
                                Column('name', String(100)),
                                Column('nationality', Text))


meta.create_all(engine)