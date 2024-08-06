from sqlalchemy import create_engine, MetaData, Table, Column, Text, insert, select, Connection
from sqlalchemy_utils import database_exists, create_database
import logging
from logging_config import config
config


class Articles:

    def __init__(self):
        try:
            engine = create_engine('postgresql://postgres:1337@localhost:5432/articles')
            metadata = MetaData()
            self.articles = Table('articles', metadata, 
                        Column('hash', Text, nullable=True),
                        Column('text', Text))
            if not database_exists(engine.url):
                create_database(engine.url)
                metadata.create_all(engine)
                
            else:
                self.connection = engine.connect()    
                

        except Exception as e:
            logging.error(e)

    def insert_data(self, hash: str, text: str):
        insrt = insert(self.articles).values(hash=hash, text=text)
        self.connection.execute(insrt)
        self.connection.commit()
        self.connection.close()

    def select_data_check(self, hash: str) -> select:
        try:
            slct = select(self.articles).where(self.articles.c.hash == hash)
            response = self.connection.execute(slct)
            for res in response:
                return res 
        except Exception as e:
            logging.error(e)
        finally:
            self.connection.close()
        