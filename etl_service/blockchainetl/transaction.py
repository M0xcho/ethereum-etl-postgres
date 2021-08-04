from dotenv import load_dotenv
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert
from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

class Transaction():
        def __init__(self):
                load_dotenv()
                self.databaseGateway = DatabaseGateway()
                self.metadata = MetaData()
                self.transactions_table = Table("transactions", self.metadata, autoload_with=self.databaseGateway.engine)
                self.conn = self.databaseGateway.engine.connect()

        def insert_transaction(self,row):
                stmt = insert(self.transactions_table).values(
                hash=row["hash"],
                nonce=row["nonce"],
                transaction_index=row["transaction_index"],
                from_address=row["from_address"],
                to_address =row["to_address"],
                value=row["value"],
                gas=row["gas"],
                gas_price=row["gas_price"],
                input=row["input"],
                receipt_cumulative_gas_used=row["receipt_cumulative_gas_used"],
                receipt_gas_used=row["receipt_gas_used"],
                receipt_contract_address=row["receipt_contract_address"],
                receipt_root=row["receipt_root"],
                receipt_status=row["receipt_status"],
                block_timestamp=row["item_timestamp"],
                block_number=row["block_number"],
                block_hash=row["block_hash"],
                )
                print(stmt)
                compiled = stmt.compile()
                print(compiled.params)
                self.conn.execute(stmt)