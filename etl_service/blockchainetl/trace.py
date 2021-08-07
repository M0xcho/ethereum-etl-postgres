from dotenv import load_dotenv
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert
from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

class Trace():
        def __init__(self):
                load_dotenv()
                self.databaseGateway = DatabaseGateway()
                self.metadata = MetaData()
                self.traces = Table("traces", self.metadata, autoload_with=self.databaseGateway.engine)
                self.conn = self.databaseGateway.engine.connect()

        def insert_trace(self,row):
                stmt = insert(self.tokens).values(
                transaction_hash=row["transaction_hash"],
                transaction_index=row["transaction_index"],
                from_address=row["from_address"],
                to_address=row["to_address"],
                value=row["value"],
                input=row["input"],
                output=row["output"],
                trace_type=row["trace_type"],
                call_type=row["call_type"],
                reward_type=row["reward_type"],
                gas=row["gas"],
                gas_used=row["gas_used"],
                subtraces=row["subtraces"],
                trace_address=row["trace_address"],
                error=row["error"],
                status=row["status"],
                block_timestamp=row["item_timestamp"],
                block_number=row["block_number"],
                block_hash=row["block_hash"],
                trace_id=row["trace_id"],        
                )
                
                print(stmt)
                compiled = stmt.compile()
                print(compiled.params)
                self.conn.execute(stmt)