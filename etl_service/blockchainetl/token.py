from dotenv import load_dotenv
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert
from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

class Token():
        def __init__(self):
                load_dotenv()
                self.databaseGateway = DatabaseGateway()
                self.metadata = MetaData()
                self.tokens = Table("tokens", self.metadata, autoload_with=self.databaseGateway.engine)
                self.conn = self.databaseGateway.engine.connect()

        def insert_token(self,row):
                stmt = insert(self.tokens).values(
                address=row["address"],
                name=row["name"],
                symbol=row["symbol"],
                decimals=row["decimals"],                
                )
                print(stmt)
                compiled = stmt.compile()
                print(compiled.params)
                self.conn.execute(stmt)