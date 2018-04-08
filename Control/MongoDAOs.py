from sys import path
path.append("..")

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


class CopyDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Copy"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

    def insert(self, copy):
        entry = {
            "lent": copy.lent,
            "book": copy.book.name
        }

        self.collection.insert(entry)

    def remove(self, copy):
        book_name = copy.book.name

        entry = {"$and": {"name" : book_name, "lent": False}}

        cp = self.collection.find_one(entry)

        if cp is None:
            raise Exception("no unlent copies from %s" % book_name)

        self.collection.remove(cp)

    def update_lent(self, id, lent):
        filter = {"_id": id}
        update = {"lent": lent}
        self.collection.update_one(filter, {"$set": update}, upsert=False)

    def get_any_from_book_name(self, book_name):
        query = self.collection.find_one({"book": book_name})

        lent = query["lent"]
        book = BookDAO(self.db).get_from_name(book_name)

        copy = Copy(lent, book)
        return copy

    def get_unlent_from_book_name(self, book_name):
        query = self.collection.find_one({"$and" : {"book": book_name, "lent": False} })

        if query is None:
            raise Exception("no unlent copy from %s" % book_name)

        book = BookDAO(self.db).get_from_name(book_name)

        copy = Copy(False, book)
        return copy


class LoanDAO:

    def __init__(self, db):
        self.db = db
        self.collection = db["Loan"]

    def delete_table(self):
        self.db.drop_collection(self.collection)

    def insert(self, loan):
        entry = {
            "loan_date": loan.loan_date,
            "return_date": loan.return_date,
            "copy": loan.copy.book.name,
            "user": loan.user.name
        }

        self.collection.insert(entry)

    def remove(self, loan):
        book_name = loan.copy.book.name
        user_name = loan.user.name
        query = {"$and" : {"copy":book_name, "user":user_name}}
        ln = self.collection.find_one(query)

        if ln is None:
            raise Exception("No loan from %s with %s" % (user_name, book_name))

        self.collection.remove(ln)

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

    