import argparse
import psycopg2
from infrastructure.persistance.repository import Repository

parser = argparse.ArgumentParser(description='Create database table')
parser.add_argument('-host', '--host', required=True, type=str, help='Hostname.')
parser.add_argument('-p', '--port', required=True, type=int, help='Connection port.')
parser.add_argument('-db', '--database', required=True, type=str, help='Database name.')
parser.add_argument('-u', '--user', required=True, type=str, help='Username')
parser.add_argument('-pw', '--password', required=False, type=str, help='User password')

args = parser.parse_args()

repo = Repository(args)
conn = repo.connect()

cur = conn.cursor()

cur.execute(open("../schema/blocks.sql", "r").read())
cur.execute(open("../schema/contracts.sql", "r").read())
cur.execute(open("../schema/logs.sql", "r").read())
cur.execute(open("../schema/token_transfers.sql", "r").read())
cur.execute(open("../schema/tokens.sql", "r").read())
cur.execute(open("../schema/traces.sql", "r").read())
cur.execute(open("../schema/transactions.sql", "r").read())

conn.commit()

cur.close()
conn.close()