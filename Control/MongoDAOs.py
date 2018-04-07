from sys import path
path.append("..")

from Model.Models import *


class AuthorDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Author"]

    def delete_table(self):
        self.collection.remove()

    def insert(self, author):
        entry = {
            "name" : author.name,
            "address": author.address,
            "telephone": author.telephone
        }

        self.collection.insert(entry)

    def remove(self, author):
        if isinstance(author, str):
            name = author
        elif isinstance(author, Author):
            name = author.name
        entry = { "name" : name }

        self.collection.remove(entry)

    def update_name(self, old_name, new_name):
        filter = {"name" : old_name}
        update = {"name" : new_name}
        self.collection.update_one(filter, {"$set": update}, upsert = False)

    def update_address(self, name, address):
        filter = {"name" : name}
        update = {"address" : address}
        self.collection.update_one(filter, {"$set": update}, upsert = False)

    def update_telephone(self, name, telephone):
        filter = {"name" : name}
        update = {"telephone" : telephone}
        self.collection.update_one(filter, {"$set": update}, upsert = False)

    def update(self, name, author):
        filter = {"name" : name}
        update = {
            "name" : author.name,
            "address": author.address,
            "telephone": author.telephone
        }
        self.collection.update_one(filter, {"$set": update}, upsert = False)

    def get_from_name(self, name):
        query = self.collection.find_one({"name" : name})

        address = query["address"]
        telephone = query["telephone"]

        author = Author(name, address, telephone)
        return author


class PublisherDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Publisher"]

    def delete_table(self):
        self.collection.remove()

    def insert(self, publisher):
        entry = {
            "name": publisher.name,
            "address": publisher.address,
            "telephone": publisher.telephone
        }

        self.collection.insert(entry)

    def remove(self, publisher):
        if isinstance(publisher, str):
            name = publisher
        elif isinstance(publisher, Publisher):
            name = publisher.name
        entry = {"name": name}

        self.collection.remove(entry)

    def update_name(self, old_name, new_name):
        filter = {"name": old_name}
        update = {"name": new_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_address(self, name, address):
        filter = {"name": name}
        update = {"address": address}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_telephone(self, name, telephone):
        filter = {"name": name}
        update = {"telephone": telephone}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update(self, name, publisher):
        filter = {"name": name}
        update = {
            "name": publisher.name,
            "address": publisher.address,
            "telephone": publisher.telephone
        }
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def get_from_name(self, name):
        query = self.collection.find_one({"name": name})

        address = query["address"]
        telephone = query["telephone"]

        publiher = Publisher(name, address, telephone)
        return publiher


class LibraryUserDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Library_user"]

    def delete_table(self):
        self.collection.remove()

    def insert(self, user):
        entry = {
            "name": user.name,
            "address": user.address,
            "telephone": user.telephone,
            "student": user.student
        }

        self.collection.insert(entry)

    def remove(self, user):
        if isinstance(user, str):
            name = user
        elif isinstance(user, LibraryUser):
            name = user.name
        entry = {"name": name}

        self.collection.remove(entry)

    def update_name(self, old_name, new_name):
        filter = {"name": old_name}
        update = {"name": new_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_address(self, name, address):
        filter = {"name": name}
        update = {"address": address}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_telephone(self, name, telephone):
        filter = {"name": name}
        update = {"telephone": telephone}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update(self, name, publisher):
        filter = {"name": name}
        update = {
            "name": publisher.name,
            "address": publisher.address,
            "telephone": publisher.telephone
        }
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def get_from_name(self, name):
        query = self.collection.find_one({"name": name})

        address = query["address"]
        telephone = query["telephone"]

        publiher = Publisher(name, address, telephone)
        return publiher

class BookDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE book (id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE, keywords TEXT[], " +
                        "quantity INTEGER, publisher_id INTEGER REFERENCES  publisher (id) ON UPDATE CASCADE, " +
                        "author_id INTEGER REFERENCES author (id))")

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS book")
        CopyDAO(self.db).delete_table()

    def insert(self, book):
        sql_string = "INSERT INTO book (name, keywords, publisher, author) VALUES (%s, %s, %s, %s)"
        self.db.execute(sql_string, (book.name, book.keywords, book.publisher, book.author))

    def remove(self, book):
        if isinstance(book, str):
            name = book
        elif isinstance(book, Book):
            name = book.name

        sql_string = "DELETE FROM book WHERE name=%s"
        self.db.execute(sql_string, name)

    def update_name(self, old_name, new_name):
        sql_string = "UPDATE book SET name = %s WHERE name = %s"
        self.db.execute(sql_string, (new_name, old_name))

    def update_keywords(self, name, keywords):
        sql_string = "UPDATE book SET keywords = %s WHERE name = %s"
        self.db.execute(sql_string, (keywords, name))

    def add_keyword(self, name, keyword):
        sql_string = "UPDATE book set keywords = keyword || %s WHERE name = %s"
        self.db.execute(sql_string, (keyword, name))

    def update_quantity(self, name, quantity):
        sql_string = "UPDATE book set quantity = %s WHERE name = %s"
        self.db.execute(sql_string, (quantity, name))

    def add_copy(self, name):
        sql_string = "UPDATE book set quantity = quantity + 1 WHERE name = %s"
        self.db.execute(sql_string, (name,))

    def delete_copy(self, name):
        sql_string = "UPDATE book set quantity = quantity - 1 WHERE name = %s"
        self.db.execute(sql_string, (name,))

    def update_publisher(self, name, publisher_name):
        sql_string = "SELECT id FROM publisher WHERE name = %s"
        self.db.execute(sql_string, (publisher_name,))
        publisher_id = self.db.fetchone()[0]

        sql_string = "UPDATE book SET publisher = %s WHERE name = %s"
        self.db.execute(sql_string, (publisher_id, name))

    def update_author(self, name, author_name):
        sql_string = "SELECT id FROM author WHERE name = %s"
        self.db.execute(sql_string, (author_name,))
        author_id = self.db.fetchone()[0]
        sql_string = "UPDATE book SET author = %s WHERE name = %s"
        self.db.execute(sql_string, (author_id, name))

    def update(self, name, book):
        sql_string = "SELECT id FROM author WHERE name = %s"
        self.db.execute(sql_string, (book.author.name,))
        new_author_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM publisher WHERE name = %s"
        self.db.execute(sql_string, (book.publisher.name,))
        new_publisher_id = self.db.fetchone()[0]

        sql_string = "UPDATE book SET name = %s, keywords = %s, quantity = %s, author = %s, publisher = %s WHERE name = %s"
        self.db.execute(sql_string, (book.name, book.keywords, book.quantity, new_author_id, new_publisher_id, name))

    def get(self, id):
        sql_string = "SELECT * FROM book WHERE id = %s"
        self.db.execute(sql_string, (id,))

        try:
            row = self.db.fetchone()
            name = row[1]
            keywords = row[2]
            quantity = row[3]
            author_id = row[4]
            publisher_id = row[5]

            author = AuthorDAO(self.db).get(author_id)
            publisher = PublisherDAO(self.db).get(publisher_id)

            book = Book(name, keywords, quantity, author, publisher)
            return book

        except ProgrammingError:
            raise Exception("No book with this ID")

    def get_from_name(self, name):
        sql_string = "SELECT * FROM book WHERE name = %s"
        self.db.execute(sql_string, (name,))

        try:
            row = self.db.fetchone()
            address = row[2]
            telephone = row[3]

            author = Author(name, address, telephone)
            return author

        except ProgrammingError:
            raise Exception("No book with this name")


class CopyDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE copy (id SERIAL PRIMARY KEY,  lent BOOLEAN," +
                        " book_id INTEGER REFERENCES book (id) ON UPDATE CASCADE)")
        LoanDAO(self.db).delete_table()

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS copy")

    def insert(self, copy):
        sql_string = "SELECT id FROM book WHERE name = %s"
        self.db.execute(sql_string, (copy.book.name,))
        book_id = self.db.fetchone()[0]

        sql_string = "INSERT INTO copy (lent, book) VALUES (%s, %s)"
        self.db.execute(sql_string, (copy.lent, book_id))

        BookDAO.add_copy(copy.book.name)

    def remove(self, copy):
        sql_string = "SELECT id FROM book WHERE name = %s"
        self.db.execute(sql_string, (copy.book.name,))
        book_id = self.db.fetchone()[0]
        sql_string = "DELETE FROM copy WHERE book_id = %s and lent = FALSE"
        self.db.execute(sql_string, (book_id,))
        status_str = self.db.statusmessage
        status_str = status_str.split()

        if status_str[1] == 0:
            raise Exception("all copies lent")
        else:
            BookDAO.delete_copy(copy.book.name)

    def update_lent(self, id, lent):
        sql_string = "UPDATE copy SET lent = %s WHERE id = %s"
        self.db.execute(sql_string, (lent, id))

    def get(self, id):
        sql_string = "SELECT * FROM copy WHERE id = %s"
        self.db.execute(sql_string, (id,))

        try:
            row = self.db.fetchone()
            lent = row[1]
            book_id = row[2]

            book = BookDAO(self.db).get(book_id)

            copy = Copy(lent, book)
            return copy

        except ProgrammingError:
            raise Exception("No copy with this ID")

    def get_any_from_book_name(self, book_name):
        sql_string = "SELECT id FROM book WHERE name = %s"
        self.db.execute(sql_string, (book_name,))
        try:
            book_id = self.db.fetchone()[0]
        except ProgrammingError:
            raise Exception("No book with this name")

        sql_string = "SELECT * FROM copy WHERE book_id = %s"
        self.db.execute(sql_string, (book_id,))

        try:
            row = self.db.fetchone()
            lent = row[1]

            book = BookDAO(self.db).get(book_id)

            copy = Copy(lent, book)
            return copy

        except ProgrammingError:
            raise Exception("No copy of this book")

    def get_unlent_from_book_name(self, book_name):
        sql_string = "SELECT id FROM book WHERE name = %s"
        self.db.execute(sql_string, (book_name,))
        try:
            book_id = self.db.fetchone()[0]
        except ProgrammingError:
            raise Exception("No book with this name")

        sql_string = "SELECT * FROM copy WHERE book_id = %s and lent = FALSE"
        self.db.execute(sql_string, (book_id,))

        try:
            row = self.db.fetchone()
            lent = row[1]

            book = BookDAO(self.db).get(book_id)

            copy = Copy(lent, book)
            return copy

        except ProgrammingError:
            raise Exception("No unlent copy of this book")


class LoanDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE loan (id SERIAL PRIMARY KEY, loan_date DATE NOT NULL, return_date DATE, " +
                        "copy_id INTEGER NOT NULL REFERENCES copy (id) ON UPDATE CASCADE," +
                        " user_id INTEGER NOT NULL REFERENCES library_user (id) ON UPDATE CASCADE )")

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS loan CASCADE")

    def insert(self, loan):

        sql_string = "SELECT id FROM library_user WHERE name = %s"
        self.db.execute(sql_string, (loan.user.name,))
        user_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM copy WHERE lent = FALSE "
        self.db.execute(sql_string)

        if self.db.rowcount > 0:
            copy_id = self.db.fetchone()[0]

            sql_string = "INSERT INTO loan (loan_date, return_date, copy_id, user_id) VALUES (%s, %s, %s, %s)"
            self.db.execute(sql_string, (loan.loan_date, loan.return_date, copy_id, user_id))

            CopyDAO.update_lent(copy_id, True)
        else:
            raise Exception("all copies lent!")

    def remove(self, loan):

        sql_string = "SELECT id FROM library_user WHERE name = %s"
        self.db.execute(sql_string, (loan.user.name,))
        user_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM book where name = %s"
        data = (loan.copy.book.name,)
        self.db.execute(sql_string, data)
        book_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM copy WHERE book_id = %s AND lent = TRUE "
        self.db.execute(sql_string, book_id)

        if self.db.rowcount > 0:
            copy_id = self.db.fetchone()[0]

            sql_string = "DELETE FROM loan WHERE copy_id = %s AND user_id = %s"
            self.db.execute(sql_string, (copy_id, user_id))

            CopyDAO.update_lent(copy_id, False)
        else:
            raise Exception("no copies lent!")

    def get(self, id):
        sql_string = "SELECT * FROM loan WHERE id = %s"
        self.db.execute(sql_string, (id,))

        try:
            row = self.db.fetchone()
            loan_date = row[2]
            return_date = row[3]
            copy_id = row[4]
            user_id = row[5]

            copy = CopyDAO(self.db).get(copy_id)
            user = LibraryUserDAO(self.db).get(user_id)

            loan = Loan(copy, user, loan_date, return_date)
            return loan

        except ProgrammingError:
            raise Exception("No Loan with this ID")

    def get_all_from_user(self, user_id):
        sql_string = "SELECT * FROM loan WHERE user_id = %s"
        self.db.execute(sql_string, (user_id,))

        try:
            row = self.db.fetchone()
            loan_date = row[2]
            return_date = row[3]
            copy_id = row[4]

            copy = CopyDAO(self.db).get(copy_id)
            user = LibraryUserDAO(self.db).get(user_id)

            loan = Loan(copy, user, loan_date, return_date)
            return loan

        except ProgrammingError:
            raise Exception("No loan from this user")

