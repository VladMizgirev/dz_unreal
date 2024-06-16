import sqlalchemy as sq
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
#metadata = MetaData()

class Publisher(Base):
    __tablename__ = "publisher"

    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name_publisher = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__ = "book"
    id_book = sq.Column(sq.Integer, primary_key=True)
    title_publisher = sq.Column(sq.String(length=40), unique=True)
    id_publishers = sq.Column(sq.Integer, sq.ForeignKey("id_publisher"), nullable=False)
    publisher = relationship(Publisher, backref="books")

class Shop(Base):
    __tablename__ = "shop"

    id_shop = sq.Column(sq.Integer, primary_key=True)
    name_shop = sq.Column(sq.String(length=40), unique=True)

class Stock(Base):
    __tablename__ = "stock"

    id_stock = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("id_book"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("id_shop"), nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

class Sale(Base):
    __tablename__ = "sale"

    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    data_sale = sq.Column(sq.Date)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("id_stock"), nullable=False)

    stock = relationship(Stock, backref="sale")

def create_tables(engine):
    Base.metadata.create_all(engine)
