from dotenv import load_dotenv
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert
from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

class Block():
        def __init__(self):
                load_dotenv()
                self.databaseGateway = DatabaseGateway()
                self.metadata = MetaData()
                self.blocks_table = Table("blocks", self.metadata, autoload_with=self.databaseGateway.engine)
                self.conn = self.databaseGateway.engine.connect()

        def insert_block(self,row):
                stmt = insert(self.blocks_table).values(
                number=row["number"],
                hash=row["hash"],
                parent_hash=row["parent_hash"],
                nonce=row["nonce"],
                sha3_uncles=row["sha3_uncles"],
                logs_bloom=row["logs_bloom"],
                transactions_root=row["transactions_root"],
                state_root=row["state_root"],
                receipts_root=row["receipts_root"],
                miner=row["miner"],
                difficulty=row["difficulty"],
                total_difficulty=row["total_difficulty"],
                size=row["size"],
                extra_data=row["extra_data"],
                gas_limit=row["gas_limit"],
                gas_used=row["gas_used"],
                timestamp=row["item_timestamp"],
                transaction_count=row["transaction_count"]
                )
                self.conn.execute(stmt)