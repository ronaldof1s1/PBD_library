class AuthorDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT)")