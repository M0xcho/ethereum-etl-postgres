from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os

class DatabaseGateway():
    def __init__(self):
        load_dotenv()
        self.user = os.getenv('user')
        self.password = os.getenv('password')
        self.host = os.getenv('host')
        self.port = os.getenv('port')
        self.db = os.getenv('db')
        self.engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(self.user, self.password, self.host, self.port, self.db))