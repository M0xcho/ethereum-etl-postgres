from sqlalchemy.sql.schema import Index
from sqlalchemy.sql.sqltypes import ARRAY, BIGINT, INT, NUMERIC, TEXT, VARCHAR, TIMESTAMP
from infrastructure.gateways.database import DatabaseGateway
from sqlalchemy import Table, Column, MetaData

databaseGateway = DatabaseGateway()

metadata = MetaData()

blocks_table = Table("blocks",
    metadata,
    Column('timestamp', TIMESTAMP, index=True),
    Column('number', BIGINT),
    Column('hash', VARCHAR(66)),
    Column('parent_hash', VARCHAR(66)),
    Column('nonce', VARCHAR(42)),
    Column('sha3_uncles', VARCHAR(66)),
    Column('logs_bloom', TEXT),
    Column('transactions_root', VARCHAR(66)),
    Column('state_root', VARCHAR(66)),
    Column('receipts_root', VARCHAR(66)),
    Column('miner', VARCHAR(42)),
    Column('difficulty', NUMERIC(38)),
    Column('total_difficulty', NUMERIC(38)),
    Column('size', BIGINT),
    Column('extra_data', TEXT),
    Column('gas_limit', BIGINT),
    Column('gas_used', BIGINT),
    Column('transaction_count', BIGINT),
 )

contracts_table = Table("contracts", 
    metadata,
    Column('address', VARCHAR(42)),
    Column('bytecode', TEXT),
    Column('function_sighashes', ARRAY(TEXT))
)

logs_table = Table("logs", 
    metadata,
    Column('log_index', BIGINT),
    Column('transaction_hash', VARCHAR(66)),
    Column('transaction_index', BIGINT),
    Column('address', VARCHAR(42)),
    Column('data', TEXT),
    Column('topic0', VARCHAR(66)),
    Column('topic1', VARCHAR(66)),
    Column('topic2', VARCHAR(66)),
    Column('topic3', VARCHAR(66)),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BIGINT),
    Column('block_hash', VARCHAR(66))
)

token_tranfers_table = Table("token_transfers", 
    metadata,
    Column('token_address', VARCHAR(42)),
    Column('from_address', VARCHAR(42)),
    Column('to_address', VARCHAR(42)),
    Column('value', NUMERIC(78)),
    Column('transaction_hash', VARCHAR(66)),
    Column('log_index', BIGINT),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BIGINT),
    Column('block_hash', VARCHAR(66))
)

tokens_table = Table("tokens", 
    metadata,
    Column('address', VARCHAR(42)),
    Column('name', TEXT),
    Column('symbol', TEXT),
    Column('decimals', INT),
    Column('function_sighashes', ARRAY(TEXT)),
)

traces_table = Table("traces", 
    metadata,
    Column('transaction_hash', VARCHAR(66)),
    Column('transaction_index', BIGINT),
    Column('from_address', VARCHAR(42)),
    Column('to_address', VARCHAR(42)),
    Column('value', NUMERIC(38)),
    Column('input', TEXT),
    Column('output', TEXT),
    Column('trace_type', VARCHAR(16)),
    Column('call_type', VARCHAR(16)),
    Column('reward_type', VARCHAR(16)),
    Column('gas', BIGINT),
    Column('gas_used', BIGINT),
    Column('subtraces', BIGINT),
    Column('trace_address', VARCHAR(8192)),
    Column('error', TEXT),
    Column('status', INT),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BIGINT),
    Column('block_hash', VARCHAR(66)),
    Column('trace_id', TEXT),
)

transactions_table = Table("transactions", 
    metadata,
    Column('hash', VARCHAR(66)),
    Column('nonce', BIGINT),
    Column('transaction_index', BIGINT),
    Column('from_address', VARCHAR(42)),
    Column('to_address', VARCHAR(42)),
    Column('value', NUMERIC(38)),
    Column('gas', BIGINT),
    Column('gas_price', BIGINT),
    Column('input', TEXT),
    Column('receipt_cumulative_gas_used', BIGINT),
    Column('receipt_gas_used', BIGINT),
    Column('receipt_contract_address', VARCHAR(42)),
    Column('receipt_root', VARCHAR(66)),
    Column('receipt_status', BIGINT),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BIGINT),
    Column('block_number', VARCHAR(66))
)