class AuthorDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT)")

    def insert(self, author):
        self.db.execute("""INSERT INTO author (name, address, telephone) VALUES (%s, %s, %s)""",(author.name, author.address, author.telephone))

class BookDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE book (id SERIAL PRIMARY KEY, name TEXT NOT NULL, keywords TEXT[], publisher_id INTEGER REFERENCES  publisher (id), author_id INTEGER REFERENCES author (id))")


class CopyDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE copy (id SERIAL PRIMARY KEY, book_id INTEGER REFERENCES book (id), quantity INTEGER, lent BOOLEAN)")

class LoanDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE loan (id SERIAL PRIMARY KEY, loan_date DATE NOT NULL, return_date DATE, copy_id INTEGER NOT NULL REFERENCES copy (id), user_id INTEGER NOT NULL REFERENCES library_user (id) )")

class PublisherDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE publisher (id SERIAL NOT NULL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT)")

class LibraryUserDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE library_user (id SERIAL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT, student BOOLEAN NOT NULL)")

