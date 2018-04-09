
from enum import Enum, unique
from tkinter import *


@unique
class views(Enum):
    AUTHORS = 1
    PUBLISHERS = 2
    USERS = 3
    BOOKS = 4
    COPIES = 5
    LOANS = 6



class MainWindow:
    def __init__(self, master, dao_factory):

        self.dao_factory = dao_factory

        self.master = master
        master.title("Library")

        self.current_view = views.LOANS

        #WIDGETS

        self.button_frame = Frame(master, bg="LIGHTBLUE", bd=5)
        self.list_frame = Frame(master, bd=5, relief=GROOVE, bg="RED")
        self.actions_frame  = Frame(master, bg="LIGHTGREEN", bd=5)

        self.authors_button = Button(self.button_frame, text="Authors", command=self.show_authors, bg="LIGHTBLUE")
        self.publishers_button = Button(self.button_frame, text="Publishers", command=self.show_publishers, bg="LIGHTBLUE")
        self.users_button = Button(self.button_frame, text="Library users", command=self.show_users, bg="LIGHTBLUE")
        self.books_button = Button(self.button_frame, text="Books", command=self.show_books, bg="LIGHTBLUE")
        self.copies_button = Button(self.button_frame, text="Copies", command=self.show_copies, bg="LIGHTBLUE")
        self.loans_button = Button(self.button_frame, text="Loans", command=self.show_loans, bg="LIGHTBLUE")

        self.listbox = Listbox(self.list_frame)

        self.add_button = Button(self.actions_frame, text="ADD", bg="LIGHTGREEN")
        self.delete_button = Button(self.actions_frame, text="REMOVE", bg="LIGHTGREEN")
        self.edit_button = Button(self.actions_frame, text="EDIT", bg="LIGHTGREEN")


        #LAYOUT

        self.button_frame.grid(row=0, column=0, sticky=W + E + S + N)
        self.list_frame.grid(row=0, column=1, sticky=W + E + S + N)
        self.actions_frame.grid(row=0, column=2, sticky=W + E + S + N)

        self.authors_button.grid(row=0, column=0, sticky=W+E+S+N, ipady=20)
        self.publishers_button.grid(row=1, column=0, sticky=W+E+S+N, ipady=20)
        self.users_button.grid(row=2, column=0, sticky=W+E+S+N, ipady=20)
        self.books_button.grid(row=3, column=0, sticky=W+E+S+N, ipady=20)
        self.copies_button.grid(row=4, column=0, sticky=W+E+S+N, ipady=20)
        self.loans_button.grid(row=5, column=0, sticky=W+E+S+N, ipady=20)

        self.listbox.grid(sticky=W+E+S+N)

        self.add_button.grid(row=0, column=0, sticky=W+E+S+N, ipady=20)
        self.delete_button.grid(row=1, column=0, sticky=W+E+S+N, ipady=20)
        self.edit_button.grid(row=2, column=0, sticky=W+E+S+N, ipady=20)


    def show_authors(self):
        if self.current_view == views.AUTHORS:
            return

        self.listbox.delete(0,END)

        author_dao = self.dao_factory.get_AuthorDAO()
        authors = author_dao.get_all()

        self.listbox.insert(END, authors)

    def show_publishers(self):
        pass
    def show_users(self):
        pass
    def show_books(self):
        pass
    def show_copies(self):
        pass
    def show_loans(self):
        pass

