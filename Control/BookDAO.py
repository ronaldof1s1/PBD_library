class BookDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE book (id SERIAL PRIMARY KEY, name TEXT NOT NULL, keywords TEXT[], publisher_id INTEGER REFERENCES  publisher (id), author_id INTEGER REFERENCES author (id))")

