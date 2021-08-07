from dotenv import load_dotenv
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert
from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

class Contract():
        def __init__(self):
                load_dotenv()
                self.databaseGateway = DatabaseGateway()
                self.metadata = MetaData()
                self.contracts = Table("contracts", self.metadata, autoload_with=self.databaseGateway.engine)
                self.conn = self.databaseGateway.engine.connect()

        def insert_contract(self,row):
                stmt = insert(self.contracts).values(
                address=row["address"],
                bytecode=row["bytecode"],
                function_sighashes=row["function_sighashes"],                              
                )
                print(stmt)
                compiled = stmt.compile()
                print(compiled.params)
                self.conn.execute(stmt)