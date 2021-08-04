import sys
import os
import csv
from distutils.util import strtobool

from dotenv import load_dotenv
from etl_service.blockchainetl.streaming.streaming_utils import configure_signals, configure_logging
from etl_service.ethereumetl.enumeration.entity_type import EntityType

from etl_service.ethereumetl.providers.auto import get_provider_from_uri
from etl_service.ethereumetl.thread_local_proxy import ThreadLocalProxy

from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import insert

class BlocksService():
    def __init__(self):
        load_dotenv()
        self.databaseGateway = DatabaseGateway()
        self.metadata = MetaData()
        self.blocks_table = Table("blocks", self.metadata, autoload_with=self.databaseGateway.engine)
        self.conn = self.databaseGateway.engine.connect()

        self.last_synced_block_file = 'last_synced_block.txt'
        self.lag = 0
        self.provider_uri = os.getenv('rpcUri')
        self.output = "custompostgres"
        self.start_block = None
        self.entity_types = parse_entity_types("entity_types")
        self.period_seconds = 10
        self.batch_size = 10
        self.block_batch_size = 1
        self.max_workers = 5
        self.log_file = None
        self.pid_file = None

        #Stream Handler
        stream(self.last_synced_block_file, self.lag, self.provider_uri, self.output, self.start_block, self.entity_types,
        self.period_seconds, self.batch_size, self.block_batch_size, self.max_workers, self.log_file, self.pid_file)

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

def stream(self, last_synced_block_file, lag, provider_uri, output, start_block, entity_types,
           period_seconds=10, batch_size=2, block_batch_size=10, max_workers=5, log_file=None, pid_file=None):

    configure_logging(log_file)
    configure_signals()
    validate_entity_types(entity_types, output)

    from etl_service.ethereumetl.streaming.item_exporter_creator import create_item_exporter
    from etl_service.ethereumetl.streaming.eth_streamer_adapter import EthStreamerAdapter
    from etl_service.blockchainetl.streaming.streamer import Streamer

    # TODO: Implement fallback mechanism for provider uris instead of picking randomly

    streamer_adapter = EthStreamerAdapter(
        batch_web3_provider=ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True)),
        item_exporter=create_item_exporter(output),
        batch_size=batch_size,
        max_workers=max_workers,
        entity_types=entity_types
    )
    streamer = Streamer(
        blockchain_streamer_adapter=streamer_adapter,
        last_synced_block_file=last_synced_block_file,
        lag=lag,
        start_block=start_block,
        period_seconds=period_seconds,
        block_batch_size=block_batch_size,
        pid_file=pid_file
    )
    streamer.stream()

def parse_entity_types():
    entity_types = []
    if (strtobool(os.getenv('streamBlocks', 'False'))):
        return entity_types
    pass

def validate_entity_types(entity_types, output):
    from etl_service.ethereumetl.streaming.item_exporter_creator import determine_item_exporter_type, ItemExporterType
    item_exporter_type = determine_item_exporter_type(output)
    if item_exporter_type == ItemExporterType.POSTGRES \
            and (EntityType.CONTRACT in entity_types or EntityType.TOKEN in entity_types):
        raise ValueError('contract and token are not yet supported entity types for postgres item exporter.')
