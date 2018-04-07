from sys import path
path.append("..")
from Model.Models import *

class AuthorDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE, address TEXT, telephone TEXT)")

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS IF EXISTS author")
        LoanDAO(self.db).delete_table()

    def insert(self, author):
        sql_string = "INSERT INTO author (name, address, telephone) VALUES (%s, %s, %s)"
        self.db.execute(sql_string, (author.name, author.address, author.telephone))

    def remove(self, author):
        if isinstance(author,str):
            name = author
        elif isinstance(author, Author):
            name = author.name
        sql_string = "DELETE FROM author WHERE name=%s"
        self.db.execute(sql_string, name)

    def update_name(self, old_name, new_name):
        sql_string = "UPDATE author SET name = %s WHERE name = %s"
        self.db.execute(sql_string, (new_name, old_name))

    def update_address(self, name, address):
        sql_string = "UPDATE author SET address = %s WHERE name = %s"
        self.db.execute(sql_string, (address, name))

    def update_telephone(self, name, telephone):
        sql_string = "UPDATE author SET telephone = %s WHERE name = %s"
        self.db.execute(sql_string, (telephone, name))

    def update(self,name, author):
        sql_string = "UPDATE author SET name=%s, address=%s, telephone=%s WHERE name = %s"
        self.db.execute(sql_string, (author.name, author.address, author.telephone, name))


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
        self.db.execute (sql_string, (publisher_name,))
        publisher_id = self.db.fetchone()[0]

        sql_string = "UPDATE book SET publisher = %s WHERE name = %s"
        self.db.execute(sql_string, (publisher_id, name))

    def update_author(self, name, author_name):
        sql_string = "SELECT id FROM author WHERE name = %s"
        self.db.execute (sql_string, (author_name,))
        author_id = self.db.fetchone()[0]
        sql_string = "UPDATE book SET author = %s WHERE name = %s"
        self.db.execute(sql_string, (author_id, name))

    def update(self,name, book):
        sql_string = "SELECT id FROM author WHERE name = %s"
        self.db.execute(sql_string, (book.author.name,))
        new_author_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM publisher WHERE name = %s"
        self.db.execute(sql_string, (book.publisher.name,))
        new_publisher_id = self.db.fetchone()[0]

        sql_string = "UPDATE book SET name = %s, keywords = %s, quantity = %s, author = %s, publisher = %s WHERE name = %s"
        self.db.execute(sql_string, (book.name, book.keywords, book.quantity, new_author_id, new_publisher_id, name))


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

        if status_str[1] == 0 :
            raise Exception("all copies lent")
        else:
            BookDAO.delete_copy(copy.book.name)

    def update_lent(self, id, lent):
        sql_string = "UPDATE copy SET lent = %s WHERE id = %s"
        self.db.execute(sql_string, (lent, id))


class LoanDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE loan (id SERIAL PRIMARY KEY, loan_date DATE NOT NULL, return_date DATE, " +
                        "copy_id INTEGER NOT NULL REFERENCES copy (id) ON UPDATE CASCADE," +
                        " user_id INTEGER NOT NULL REFERENCES library_user (id) ON UPDATE CASCADE )")

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS IF EXISTS loan CASCADE")

    def insert(self, loan):

        sql_string = "SELECT id FROM library_user WHERE name = %s"
        self.db.execute(sql_string, (loan.user.name,))
        user_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM copy WHERE lent = FALSE "
        self.db.execute(sql_string)

        if self.db.rowcount > 0:
            copy_id = self.db.fetchone()[0]

            sql_string = "INSERT INTO loan (loan_date, return_date, copy_id, user_id) VALUES (%s, %s, %s, %s)"
            self.db.execute(sql_string,(loan.loan_date, loan.return_date, copy_id, user_id))

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

class PublisherDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE publisher (id SERIAL NOT NULL PRIMARY KEY, name TEXT NOT NULL UNIQUE, " +
                        "address TEXT, telephone TEXT)")

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS publisher")

    def insert(self, publisher):
        sql_string = "INSERT INTO publisher (name, address, telephone) VALUES (%s, %s, %s)"
        self.db.execute(sql_string, (publisher.name, publisher.address, publisher.telephone))

    def remove(self, publisher):
        if isinstance(publisher, str):
            name = publisher
        elif isinstance(publisher, Publisher):
            name = publisher.name
        sql_string = "DELETE FROM publisher WHERE name=%s"
        self.db.execute(sql_string, name)

    def update_name(self, old_name, new_name):
        sql_string = "UPDATE publisher SET name = %s WHERE name = %s"
        self.db.execute(sql_string, (new_name, old_name))

    def update_address(self, name, address):
        sql_string = "UPDATE publisher SET address = %s WHERE name = %s"
        self.db.execute(sql_string, (address, name))

    def update_telephone(self, name, telephone):
        sql_string = "UPDATE publisher SET telephone = %s WHERE name = %s"
        self.db.execute(sql_string, (telephone, name))

    def update(self, name, publisher):
        sql_string = "UPDATE publisher SET name=%s, address=%s, telephone=%s WHERE name = %s"
        self.db.execute(sql_string, (publisher.name, publisher.address, publisher.telephone, name))


class LibraryUserDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE library_user (id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE, address TEXT," +
                        " telephone TEXT, student BOOLEAN NOT NULL)")

    def delete_table(self):
        self.db.execute("DROP TABLE IF EXISTS library_user")

    def insert(self, user):
        sql_string = "INSERT INTO library_user (name, address, telephone, student) VALUES (%s, %s, %s, %s)"
        self.db.execute(sql_string, (user.name, user.address, user.telephone, user.student))

    def remove(self, user):
        if isinstance(user, str):
            name = user
        elif isinstance(user, LibraryUser):
            name = user.name
        sql_string = "DELETE FROM library_user WHERE name=%s"
        self.db.execute(sql_string, name)

    def update_name(self, old_name, new_name):
        sql_string = "UPDATE library_user SET name = %s WHERE name = %s"
        self.db.execute(sql_string, (new_name, old_name))

    def update_address(self, name, address):
        sql_string = "UPDATE library_user SET address = %s WHERE name = %s"
        self.db.execute(sql_string, (address, name))

    def update_telephone(self, name, telephone):
        sql_string = "UPDATE library_user SET telephone = %s WHERE name = %s"
        self.db.execute(sql_string, (telephone, name))

    def update_student(self, name, student):
        sql_string = "UPDATE library_user SET student = %s WHERE name = %s"
        self.db.execute(sql_string, (student, name))

    def update(self, name, user):
        sql_string = "UPDATE publisher SET name=%s, address=%s, telephone=%s, student=%s WHERE name = %s"
        self.db.execute(sql_string, (user.name, user.address, user.telephone, user.student, name))