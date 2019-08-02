import sqlalchemy as db
from decouple import config
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.orm import sessionmaker


user = config('DB_USER')
password = config('DB_PASSWORD')
server = config('DB_SERVER', default='localhost')
database = config('DB_NAME')

Base = declarative_base()
engine = db.create_engine('mysql+pymysql://{}:{}@{}/{}'.format(user, password, server, database), echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Query(Base):
    __tablename__ = 'queries'
    id = Column(Integer, primary_key=True)
    link = Column(URLType)
    email = Column(EmailType)

    def __repr__(self):
        return "Query(link={}, email={})".format(self.link, self.email)

Base.metadata.create_all(engine)

def create_query(link, email):
    query = Query(link=link, email=email)
    session.add(query)
    session.commit()

    return print("Query(link={}, email={})".format(link, email))
