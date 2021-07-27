import psycopg2

class Repository():
    def __init__(self, args):
        self.db = args.database
        self.user = args.user
        self.password = args.password
        self.host = args.host
        self.port = args.port
        
    def connect(self):
        return psycopg2.connect("dbname={} user={} password={} host={} port={}".format(self.db, self.user, self.password or None, self.host, self.port))