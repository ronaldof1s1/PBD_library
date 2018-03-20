class CopyDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE copy (id SERIAL PRIMARY KEY, book_id INTEGER REFERENCES book (id), quantity INTEGER, lent BOOLEAN)")