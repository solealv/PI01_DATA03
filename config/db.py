from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/pi_i")

meta = MetaData()

conn = engine.connect()