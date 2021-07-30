import argparse
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

cur.execute(open("../indexes/blocks.sql", "r").read())
cur.execute(open("../indexes/logs.sql", "r").read())
cur.execute(open("../indexes/token_transfers.sql", "r").read())
cur.execute(open("../indexes/traces.sql", "r").read())
cur.execute(open("../indexes/transactions.sql", "r").read())

conn.commit()

cur.close()
conn.close()