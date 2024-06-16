
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale
import json

#login = str(input())
#password = str(input())
#name_bd = str(input())
#DSN = f'postgresql+psycopg2://{login}:{password}@localhost:5432/{name_bd}'
DSN1 = 'postgresql+psycopg2://Vlad:19121996@localhost:5432/bd'
engine = sqlalchemy.create_engine(DSN1)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)
publisher1 = Publisher(name_publisher = 'mark', id_publisher = 1)
print(publisher1.id_publisher)
session.close()