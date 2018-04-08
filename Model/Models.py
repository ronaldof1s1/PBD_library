from datetime import date

class InvalidFieldException(Exception):
    pass

class InvalidRegisterException(Exception):
    pass



class Author:

    def __init__(self, name, address, telephone):
        try:
            self.validate_name(name)
            self.validate_address(address)
            self.validade_telephone(telephone)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid Author")

        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return self.name

    def validate_name(self, name):
        if name == "" or not isinstance(name, str):
            raise InvalidFieldException("invalid name")

        if not name[0].isalpha():
            raise InvalidFieldException("invalid name")

    def validate_address(self, address):
        if address == "" or not isinstance(address, str):
            raise InvalidFieldException("invalid address")

    def validate_telephone(self,telephone):
        if telephone == "" or not telephone.isdigit():
            raise InvalidFieldException("invalid telephone")

        if telephone.len() != 9 or not isinstance(telephone, str):
            raise InvalidFieldException("invalid telephone")


class Book:

    def __init__(self, name, keywords, quantity, publisher, author):

        try:
            self.validate_name(name)
            self.validate_keywords(keywords)
            self.validade_quantity(quantity)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid Book")

        self.name = name
        self.keywords = keywords
        self.publisher = publisher
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return self.name

    def validate_name(self, name):
        if name == "" or not isinstance(name, str):
            raise InvalidFieldException("invalid name")

    def validate_quantity(self, quantity):
        if quantity < 0 or not isinstance(quantity, int):
            raise InvalidFieldException("invalid quantity")

    def validate_keywords(self, keywords):
        if keywords == [] or not keywords[0] == "" or not isinstance(keywords[0], str):
            raise InvalidFieldException("invalid telephone")


class Copy:

    def __init__(self, lent, book):
        self.lent = lent
        self.book = book

    def __str__(self):
        return self.book.name + " exemplar"


class LibraryUser:

    def __init__(self, name, address, telephone, student):

        try:
            self.validate_name(name)
            self.validate_address(address)
            self.validade_telephone(telephone)
            self.validate_student(student)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid User")

        self.name = name
        self.address = address
        self.telephone = telephone
        self.student = student

    def __str__(self):
        return self.name

    def validate_name(self, name):
        if name == "" or not isinstance(name, str):
            raise InvalidFieldException("invalid name")

        if not name[0].isalpha():
            raise InvalidFieldException("invalid name")

    def validate_address(self, address):
        if address == "" or not isinstance(address, str):
            raise InvalidFieldException("invalid address")

    def validate_telephone(self,telephone):
        if telephone == "" or not telephone.isdigit():
            raise InvalidFieldException("invalid telephone")

        if telephone.len() != 9 or not isinstance(telephone, str):
            raise InvalidFieldException("invalid telephone")

    def validade_student(self,student):
        if not isinstance(student, bool):
            raise InvalidFieldException("invalid Student")


class Loan:

    def __init__(self, copy, user, loan_date = date.today(), return_date = date.max):

        try:
            self.validate_loan_date(loan_date)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid Loan")

        self.loan_date = loan_date
        try:
            self.validate_return_date(return_date)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid Loan")

        self.return_date = return_date

        self.copy = copy

        self.user = user

    def __str__(self):
        return self.copy + " -> " + self.user

    def validate_loan_date(self, loan_date):
        if loan_date > date.today() or not isinstance(loan_date, date):
            raise InvalidFieldException("invalid loan_date")

    def validate_return_date(self, return_date):
        if return_date < self.loan_date or return_date < date.today() or not isinstance(return_date, date):
            raise InvalidFieldException("invalid return date")


class Publisher:

    def __init__(self, name, address, telephone):

        try:
            self.validate_name(name)
            self.validate_address(address)
            self.validade_telephone(telephone)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid publisher")

        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return self.name


    def validate_name(self, name):
        if name == "" or not isinstance(name, str):
            raise InvalidFieldException("invalid name")

        if not name[0].isalpha():
            raise InvalidFieldException("invalid name")

    def validate_address(self, address):
        if address == "" or not isinstance(address, str):
            raise InvalidFieldException("invalid address")

    def validate_telephone(self,telephone):
        if telephone == "" or not telephone.isdigit():
            raise InvalidFieldException("invalid telephone")

        if telephone.len() != 9 or not isinstance(telephone, str):
            raise InvalidFieldException("invalid telephone")