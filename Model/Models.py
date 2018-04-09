from datetime import datetime

class InvalidFieldException(Exception):
    pass

class InvalidRegisterException(Exception):
    pass



class Author:

    def __init__(self, name, address, telephone):
        try:
            self.validate_name(name)
            self.validate_address(address)
            self.validate_telephone(telephone)
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
        if not isinstance(address, str):
            raise InvalidFieldException("invalid address")

    def validate_telephone(self,telephone):
        if not telephone == "":
            if not telephone.isdigit() or not isinstance(telephone, str):
                raise InvalidFieldException("invalid telephone")



class Book:

    def __init__(self, name, keywords, quantity, publisher, author):

        try:
            self.validate_name(name)
            self.validate_keywords(keywords)
            self.validate_quantity(quantity)
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
        if not isinstance(quantity, int) or quantity < 0 :
            raise InvalidFieldException("invalid quantity")

    def validate_keywords(self, keywords):
        if keywords != []:
            if not isinstance(keywords[0], str):
                raise InvalidFieldException("invalid keywords")


class Copy:

    def __init__(self, id, lent, book):

        try:
            self.validate_id(id)
        except InvalidFieldException:
            raise InvalidRegisterException("Invalid Copy")

        self.id = id
        self.lent = lent
        self.book = book

    def __str__(self):
        return str(self.id) + " - " + self.book.name + ": " + str(self.lent)

    def validate_id(self, id):
        if not isinstance(id, int) or id < 1:
            raise InvalidFieldException("invalid ID")


class LibraryUser:

    def __init__(self, name, address, telephone, student):

        try:
            self.validate_name(name)
            self.validate_address(address)
            self.validate_telephone(telephone)
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
        if not isinstance(address, str):
            raise InvalidFieldException("invalid address")

    def validate_telephone(self,telephone):
        if not telephone == "":
            if not telephone.isdigit() or not isinstance(telephone, str):
                raise InvalidFieldException("invalid telephone")

    def validate_student(self,student):
        if not isinstance(student, bool):
            raise InvalidFieldException("invalid Student")


class Loan:

    def __init__(self, copy, user, loan_date = datetime.today(), return_date = datetime.max):

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
        return str(self.copy) + " -> " + str(self.user)

    def validate_loan_date(self, loan_date):
        if loan_date > datetime.today() or not isinstance(loan_date, datetime):
            raise InvalidFieldException("invalid loan_date")

    def validate_return_date(self, return_date):
        if return_date < self.loan_date or return_date < datetime.today() or not isinstance(return_date, datetime):
            raise InvalidFieldException("invalid return date")


class Publisher:

    def __init__(self, name, address, telephone):

        try:
            self.validate_name(name)
            self.validate_address(address)
            self.validate_telephone(telephone)
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
        if not isinstance(address, str):
            raise InvalidFieldException("invalid address")

    def validate_telephone(self,telephone):
        if not telephone == "":
            if not telephone.isdigit() or not isinstance(telephone, str):
                raise InvalidFieldException("invalid telephone")
