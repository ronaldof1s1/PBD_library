class AuthorDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT)")

    def delete_table(self):
        self.db.execute("DROP TABLE author")
        LoanDAO(self.db).delete_table()

    def insert(self, author):
        self.db.execute("""INSERT INTO author (name, address, telephone) VALUES (%s, %s, %s)""",
                        (author.name, author.address, author.telephone))

class BookDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE book (id SERIAL PRIMARY KEY, name TEXT NOT NULL, keywords TEXT[]," +
                        " publisher_id INTEGER REFERENCES  publisher (id), author_id INTEGER REFERENCES author (id))")

    def delete_table(self):
        self.db.execute("DROP TABLE book")
        CopyDAO(self.db).delete_table()


    def insert(self, book):
        self.db.execute("""INSERT INTO book (name, keywords, publisher, author) VALUES (%s, %s, %s, %s)""",
                        (book.name, book.keywords, book.publisher, book.author))

class CopyDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE copy (id SERIAL PRIMARY KEY, book_id INTEGER REFERENCES book (id), quantity INTEGER, lent BOOLEAN)")
        LoanDAO(self.db).delete_table()

    def delete_table(self):
        self.db.execute("DROP TABLE copy")

    def insert(self, copy):
        self.db.execute("""INSERT INTO copy (book, quantity, lent) VALUES (%s, %s, %s)""",
                        (copy.book, copy.quantity, copy.lent))
class LoanDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE loan (id SERIAL PRIMARY KEY, loan_date DATE NOT NULL, return_date DATE, " +
                        "copy_id INTEGER NOT NULL REFERENCES copy (id)," +
                        " user_id INTEGER NOT NULL REFERENCES library_user (id) )")

    def delete_table(self):
        self.db.execute("DROP TABLE loan")

    def insert(self, loan):
        self.db.execute("""INSERT INTO loan (loan_date, return_date, copy_id, user_id) VALUES (%s, %s, %s, %s)""",
                        (loan.loan_date, loan.return_date, loan.copy, loan.user))

class PublisherDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE publisher (id SERIAL NOT NULL PRIMARY KEY, name TEXT NOT NULL, address TEXT, telephone TEXT)")

    def delete_table(self):
        self.db.execute("DROP TABLE publisher")

    def insert(self, publisher):
        self.db.execute("""INSERT INTO publisher (name, address, telephone) VALUES (%s, %s, %s)""",
                        (publisher.name, publisher.address, publisher.telephone))
class LibraryUserDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE library_user (id SERIAL PRIMARY KEY, name TEXT NOT NULL, address TEXT," +
                        " telephone TEXT, student BOOLEAN NOT NULL)")

    def delete_table(self):
        self.db.execute("DROP TABLE library_user")

    def insert(self, user):
        self.db.execute("""INSERT INTO library_user (name, address, telephone, student) VALUES (%s, %s, %s, %s)""",
                        (user.name, user.address, user.telephone, user.student))