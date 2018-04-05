from datetime import date

class Author:

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return self.name

class Book:

    def __init__(self, name, keywords, quantity, publisher, author):
        self.name = name
        self.keywords = keywords
        self.publisher = publisher
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return self.name


class Copy:

    def __init__(self, lent, book):
        self.lent = lent
        self.book = book

    def __str__(self):
        return self.book.name + " exemplar"


class LibraryUser:

    def __init__(self, name, address, telephone, student):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.student = student

    def __str__(self):
        return self.name


class Loan:

    def __init__(self, copy, user, loan_date = date.now(), return_date = date.MAXYEAR):
        self.loan_date = loan_date
        self.return_date = return_date
        self.copy = copy
        self.user = user

    def __str__(self):
        return self.copy + " -> " + self.user


class Publisher:

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone