class PublisherDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE publisher (id SERIAL NOT NULL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT)")

