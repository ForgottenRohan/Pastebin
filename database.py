from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
from logging_config import config


Base = declarative_base()
config
# Определение таблицы
class MyData(Base):
    __tablename__ = 'articles'

    hash = Column(String, primary_key=True)
    text = Column(Text, nullable=False)

class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        
        # Создание таблиц, если они не существуют
        Base.metadata.create_all(self.engine)
        logging.info('Success database connect')


    def insert_data(self, hash, text):
        session = self.Session()
        new_entry = MyData(hash=hash, text=text)
        session.add(new_entry)
        session.commit()
        session.close()
        logging.info('Data inserted')


    def select_data(self, hash):
        session = self.Session()
        entry = session.query(MyData).filter_by(hash=hash).first()  # Поиск записи по hash
        session.close()
        logging.info('Data selected')
        
        if entry:  # Если запись найдена
            return [entry.hash, entry.text]
        else:  # Если запись не найдена
            return None