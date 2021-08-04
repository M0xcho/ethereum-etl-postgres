from dotenv import load_dotenv
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert
from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

class TokenTransfer():
        def __init__(self):
                load_dotenv()
                self.databaseGateway = DatabaseGateway()
                self.metadata = MetaData()
                self.token_transfers = Table("token_transfers", self.metadata, autoload_with=self.databaseGateway.engine)
                self.conn = self.databaseGateway.engine.connect()

        def insert_token_transfer(self,row):
                stmt = insert(self.token_transfers).values(
                token_address=row["token_address"],
                from_address=row["from_address"],
                to_address=row["to_address"],
                value=row["value"],
                transaction_hash=row["transaction_hash"],
                log_index=row["log_index"],
                block_timestamp=row["item_timestamp"],
                block_number=row["block_number"],
                block_hash=row["block_hash"],
                )
                print(stmt)
                compiled = stmt.compile()
                print(compiled.params)
                self.conn.execute(stmt)