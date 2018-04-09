from sys import path
path.append("..")
from datetime import datetime

from Model.Models import *


class AuthorDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Author"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

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

        try:
            Author.validate_name(new_name)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name" : old_name}
        update = {"name" : new_name}
        self.collection.update_one(filter, {"$set": update}, upsert = False)

    def update_address(self, name, address):

        try:
            Author.validate_address(address)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name" : name}
        update = {"address" : address}
        self.collection.update_one(filter, {"$set": update}, upsert = False)

    def update_telephone(self, name, telephone):

        try:
            Author.validate_telephone(telephone)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid telephone")

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

    def get_all(self):
        rows = self.collection.find({})
        authors = []

        for row in rows:
            name = row["name"]
            address = row["address"]
            telephone = row["telephone"]

            author = Author(name, address, telephone)
            authors.append(author)

        return authors


class PublisherDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Publisher"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

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

        try:
            Publisher.validate_name(new_name)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": old_name}
        update = {"name": new_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_address(self, name, address):

        try:
            Publisher.validate_address(address)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": name}
        update = {"address": address}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_telephone(self, name, telephone):

        try:
            Publisher.validate_telephone(telephone)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid telephone")

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

        publisher = Publisher(name, address, telephone)
        return publisher

    def get_all(self):
        rows = self.collection.find({})
        publishers = []

        for row in rows:
            name = row["name"]
            address = row["address"]
            telephone = row["telephone"]

            publisher = Publisher(name, address, telephone)
            publishers.append(publisher)

        return publishers


class LibraryUserDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Library_user"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

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

        try:
            LibraryUser.validate_name(new_name)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": old_name}
        update = {"name": new_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_address(self, name, address):

        try:
            LibraryUser.validate_address(address)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid address")

        filter = {"name": name}
        update = {"address": address}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_telephone(self, name, telephone):
        try:
            LibraryUser.validate_telephone(telephone)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": name}
        update = {"telephone": telephone}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_student(self, name, student):
        try:
            LibraryUser.validate_student(student)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": name}
        update = {"student": student}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update(self, name, user):
        filter = {"name": name}
        update = {
            "name": user.name,
            "address": user.address,
            "telephone": user.telephone,
            "student": user.student
        }
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def get_from_name(self, name):
        query = self.collection.find_one({"name": name})

        address = query["address"]
        telephone = query["telephone"]
        student = query["student"]

        user = LibraryUser(name, address, telephone, student)
        return user

    def get_all(self):
        rows = self.collection.find({})
        users = []

        for row in rows:
            name = row["name"]
            address = row["address"]
            telephone = row["telephone"]
            student = row["student"]

            user = LibraryUser(name, address, telephone, student)
            users.append(user)

        return users


class BookDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Book"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

    def insert(self, book):
        entry = {
            "name": book.name,
            "keywords": book.keywords,
            "quantity": book.quantity,
            "author": book.author.name,
            "publisher": book.publisher.name
        }

        self.collection.insert(entry)

    def remove(self, book):
        if isinstance(book, str):
            name = book
        elif isinstance(book, Book):
            name = book.name
        entry = {"name": name}

        self.collection.remove(entry)

    def update_name(self, old_name, new_name):
        try:
            Book.validate_name(new_name)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": old_name}
        update = {"name": new_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_keywords(self, name, keywords):
        try:
            Book.validate_keywords(keywords)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": name}
        update = {"keywords": keywords}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def add_keyword(self, name, keyword):
        filter = {"name": name}
        update = {"keyword": keyword}
        self.collection.update_one(filter, {"$push": update}, upsert=False)

    def update_quantity(self, name, quantity):
        try:
            Book.validate_quantity(quantity)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid name")

        filter = {"name": name}
        update = {"quantity": quantity}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def add_copy(self, name):
        filter = {"name": name}
        update = {"quantity": 1}
        self.collection.update_one(filter, {"$inc": update}, upsert=False)

    def delete_copy(self, name):
        filter = {"name": name}
        update = {"quantity": -1}
        self.collection.update_one(filter, {"$inc": update}, upsert=False)

    def update_publisher(self, name, publisher_name):

        filter = {"name": name}
        update = {"publisher": publisher_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_author(self, name, author_name):
        filter = {"name": name}
        update = {"author": author_name}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update(self, name, book):
        filter = {"name": name}
        update = {
            "name": book.name,
            "keywords": book.keywords,
            "quantity": book.quantity,
            "author": book.author.name,
            "publisher": book.publisher.name
        }
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def get_from_name(self, name):
        query = self.collection.find_one({"name": name})

        keywords = query["keywords"]
        quantity = query["quantity"]
        author_name = query["author"]
        author = AuthorDAO(self.db).get_from_name(author_name)
        publisher_name = query["publisher"]
        publisher = PublisherDAO(self.db).get_from_name(publisher_name)

        book = Book(name, keywords, quantity, publisher, author)
        return book

    def get_all(self):
        rows = self.collection.find({})
        books = []

        for row in rows:
            name = row["name"]
            keywords = row["keywords"]
            quantity = row["quantity"]
            publisher_name = row["publisher"]
            author_name = row["author"]

            publisher = PublisherDAO(self.db).get_from_name(publisher_name)
            author = AuthorDAO(self.db).get_from_name(author_name)

            book = Book(name, keywords, quantity, publisher, author)
            books.append(book)

        return books


class CopyDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Copy"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

    def insert(self, copy):
        entry = {
            "id": copy.id,
            "lent": copy.lent,
            "book": copy.book.name
        }

        self.collection.insert(entry)

    def remove(self, copy):

        self.collection.remove(copy.id)

    def update_lent(self, id, lent):
        filter = {"id": id}
        update = {"lent": lent}
        self.collection.update_one(filter, {'$set': update}, upsert=False)

    def update(self, id, copy):
        filter = {"id": id}
        update = {"id":copy.id, "lent":copy.lent, "book":copy.book.name}

        self.collection.update_one(filter, {'$set': update}, upsert=False)

    def get(self, id):
        query = self.collection.find_one({"id": id})

        book_name = query["book"]
        lent = query["lent"]
        book = BookDAO(self.db).get_from_name(book_name)

        copy = Copy(id, lent, book)
        return copy

    def get_any_from_book_name(self, book_name):
        query = self.collection.find_one({"book": book_name})

        id = query["id"]
        lent = query["lent"]
        book = BookDAO(self.db).get_from_name(book_name)

        copy = Copy(id, lent, book)
        return copy

    def get_unlent_from_book_name(self, book_name):
        query = self.collection.find_one({"$and" : [{"book": book_name}, {"lent": False}] })

        if query is None:
            raise Exception("no unlent copy from %s" % book_name)

        id = query["id"]
        book = BookDAO(self.db).get_from_name(book_name)

        copy = Copy(id, False, book)
        return copy

    def get_all(self):
        rows = self.collection.find({})
        copies = []

        for row in rows:
            id = row["id"]
            lent = row["lent"]
            book_name = row["book"]

            book = BookDAO(self.db).get_from_name(book_name)

            copy = Copy(id, lent, book)
            copies.append(copy)

        return copies


class LoanDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Loan"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

    def insert(self, loan):

        copy_id = loan.copy.id
        entry = {
            "loan_date": loan.loan_date,
            "return_date": loan.return_date,
            "copy": copy_id,
            "user": loan.user.name
        }
        copydao = CopyDAO(self.db)
        copydao.update_lent(copy_id, True)

        self.collection.insert(entry)

    def remove(self, loan):
        copy_id = loan.copy.id
        user_name = loan.user.name
        query = {"$and" : [{"copy":copy_id}, {"user":user_name}]}
        ln = self.collection.find_one(query)

        if ln is None:
            raise Exception("No loan from %s with %s" % (user_name, copy_id))

        self.collection.remove(ln)

        CopyDAO(self.db).update_lent(copy_id, False)

    def update(self, copy_id, loan):
        filter = {"copy": copy_id}
        update = {"loan_date": loan.loan_date, "return_date": loan.return_date, "copy": loan.copy, "user":loan.user}

        self.collection.update_one(filter, {'$set': update}, upsert=False)

    def update_loan_date(self, id, loan_date):
        try:
            Loan.validate_loan_date(loan_date)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid loan date")

        filter = {"_id": id}
        update = {"loan_date": loan_date}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def update_return_date(self, id, return_date):
        try:
            Loan.validate_return_date(return_date)
        except InvalidFieldException:
            raise InvalidFieldException("Invalid return date")

        filter = {"_id": id}
        update = {"return_date": return_date}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def get(self, id):
        row = self.collection.find_one({"_id" : id})

        loan_date = row["loan_date"]
        return_date = row["return_date"]
        copy_id = row["copy"]
        user_name = row["user"]

        copy = CopyDAO(self.db).get(copy_id)
        user = LibraryUserDAO(self.db).get_from_name(user_name)

        loan = Loan(copy, user,loan_date, return_date)

        return loan

    def get_from_copy_id(self, id):
        row = self.collection.find_one({"copy": id})

        loan_date = row["loan_date"]
        return_date = row["return_date"]
        user_name = row["user"]

        copy = CopyDAO(self.db).get(id)
        user = LibraryUserDAO(self.db).get_from_name(user_name)

        loan = Loan(copy, user, loan_date, return_date)

        return loan

    def get_all_from_user(self, user_name):
        rows = self.collection.find({"user":user_name})
        loans = []

        for row in rows:
            loan_date = row["loan_date"]
            return_date = row["return_date"]
            copy_id = row["copy"]

            copy = CopyDAO(self.db).get(copy_id)
            user = LibraryUserDAO(self.db).get_from_name(user_name)

            loan = Loan(copy, user, loan_date, return_date)
            loans.append(loan)

        return loans

    def get_all(self):
        rows = self.collection.find({})
        loans = []

        for row in rows:
            loan_date = row["loan_date"]
            return_date = row["return_date"]
            copy_id = row["copy"]
            user_name = row["user"]

            copy = CopyDAO(self.db).get(copy_id)
            user = LibraryUserDAO(self.db).get_from_name(user_name)

            loan = Loan(copy, user, loan_date, return_date)
            loans.append(loan)

        return loans