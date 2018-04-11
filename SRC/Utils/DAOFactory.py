from sys import path
path.append("..")

from Control import *

class DAOFactory():
    def __init__(self, db_type, db):
        self.db_type = db_type
        self.db = db

    def get_AuthorDAO(self):
        
        if self.db_type == "Postgresql":
            return PostgresqlDAOs.AuthorDAO(self.db)
        elif self.db_type == "MongoDB":
            return MongoDAOs.AuthorDAO(self.db)
        else:
            raise Exception("NO DATABASE")


    def get_PublisherDAO(self):
        if self.db_type == "Postgresql":
            return PostgresqlDAOs.PublisherDAO(self.db)
        elif self.db_type == "MongoDB":
            return MongoDAOs.PublisherDAO(self.db)
        else:
            raise Exception("NO DATABASE")


    def get_UserDAO(self):
        if self.db_type == "Postgresql":
            return PostgresqlDAOs.LibraryUserDAO(self.db)
        elif self.db_type == "MongoDB":
            return MongoDAOs.LibraryUserDAO(self.db)
        else:
            raise Exception("NO DATABASE")



    def get_BookDAO(self):
        if self.db_type == "Postgresql":
            return PostgresqlDAOs.BookDAO(self.db)
        elif self.db_type == "MongoDB":
            return MongoDAOs.BookDAO(self.db)
        else:
            raise Exception("NO DATABASE")



    def get_CopyDAO(self):
        if self.db_type == "Postgresql":
            return PostgresqlDAOs.CopyDAO(self.db)
        elif self.db_type == "MongoDB":
            return MongoDAOs.CopyDAO(self.db)
        else:
            raise Exception("NO DATABASE")



    def get_LoanDAO(self):
        if self.db_type == "Postgresql":
            return PostgresqlDAOs.LoanDAO(self.db)
        elif self.db_type == "MongoDB":
            return MongoDAOs.LoanDAO(self.db)
        else:
            raise Exception("NO DATABASE")