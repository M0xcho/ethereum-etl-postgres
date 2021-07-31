import sys
import os
import csv

from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert

class BlocksService():
    def __init__(self):
        self.databaseGateway = DatabaseGateway()
        self.metadata = MetaData()
        self.blocks_table = Table("blocks", self.metadata, autoload_with=self.databaseGateway.engine)
        self.conn = self.databaseGateway.engine.connect()
        #mock 
        #event handler goes here
        with open('etl_service/blocks.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                line_count += 1
                self.insert_block(row)
            print(f'Processed {line_count} lines.')

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
        timestamp=row["timestamp"],
        transaction_count=row["transaction_count"]
        )
        result = self.conn.execute(stmt)
