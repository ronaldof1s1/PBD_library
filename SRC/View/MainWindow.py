
from enum import Enum, unique
from tkinter import *
from .AddWindows import *
from .EditWindows import *

@unique
class views(Enum):
    AUTHORS = 1
    PUBLISHERS = 2
    USERS = 3
    BOOKS = 4
    COPIES = 5
    LOANS = 6
    NONE = 7


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

        self.add_button = Button(self.actions_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.delete_button = Button(self.actions_frame, text="REMOVE", bg="LIGHTGREEN", command=self.delete)
        self.edit_button = Button(self.actions_frame, text="EDIT", bg="LIGHTGREEN", command=self.edit)


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


    #SHOW FUNCTIONS

    def show_authors(self):
        if self.current_view == views.AUTHORS:
            self.update()

        self.listbox.delete(0,END)

        author_dao = self.dao_factory.get_AuthorDAO()
        authors = author_dao.get_all()

        for author in authors:
            self.listbox.insert(END, author)

        self.current_view = views.AUTHORS

    def show_publishers(self):
        if self.current_view == views.PUBLISHERS:
            self.update()

        self.listbox.delete(0,END)

        publisher_dao = self.dao_factory.get_PublisherDAO()
        publishers = publisher_dao.get_all()

        self.listbox.insert(END, *publishers)

        self.current_view = views.PUBLISHERS

    def show_users(self):
        if self.current_view == views.USERS:
            self.update()

        self.listbox.delete(0,END)

        user_dao = self.dao_factory.get_UserDAO()
        users = user_dao.get_all()

        self.listbox.insert(END, *users)

        self.current_view = views.USERS

    def show_books(self):
        if self.current_view == views.BOOKS:
            self.update()

        self.listbox.delete(0,END)

        books_dao = self.dao_factory.get_BookDAO()
        books = books_dao.get_all()

        self.listbox.insert(END, *books)

        self.current_view = views.BOOKS

    def show_copies(self):
        if self.current_view == views.COPIES:
            self.update()

        self.listbox.delete(0,END)

        copy_dao = self.dao_factory.get_CopyDAO()
        copies = copy_dao.get_all()


        self.listbox.insert(END, *copies)
        self.current_view = views.COPIES

    def show_loans(self):
        if self.current_view == views.LOANS:
            self.update()

        self.listbox.delete(0,END)

        loan_dao = self.dao_factory.get_LoanDAO()
        loans = loan_dao.get_all()

        self.listbox.insert(END, *loans)
        self.current_view = views.LOANS

    #ADD FUNCTIONS

    def add(self):
        if self.current_view == views.AUTHORS:
            self.add_author()
        elif self.current_view == views.PUBLISHERS:
            self.add_publisher()
        elif self.current_view == views.USERS:
            self.add_user()
        elif self.current_view == views.BOOKS:
            self.add_book()
        elif self.current_view == views.COPIES:
            self.add_copy()
        else:
            self.add_loan()

        self.update()

    def add_author(self):

        Add_author_window(self.master, self.dao_factory)

    def add_publisher(self):
        Add_publisher_window(self.master, self.dao_factory)

    def add_user(self):
        Add_user_window(self.master, self.dao_factory)

    def add_book(self):
        Add_book_window(self.master, self.dao_factory)

    def add_copy(self):
        Add_copy_window(self.master, self.dao_factory)

    def add_loan(self):
        Add_loan_window(self.master, self.dao_factory)

    #DELETE FUNCTIONS

    def delete(self):
        if self.current_view == views.AUTHORS:
            self.delete_author()
        elif self.current_view == views.PUBLISHERS:
            self.delete_publisher()
        elif self.current_view == views.USERS:
            self.delete_user()
        elif self.current_view == views.BOOKS:
            self.delete_book()
        elif self.current_view == views.COPIES:
            self.delete_copy()
        else:
            self.delete_loan()

    def delete_author(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)

        author_dao = self.dao_factory.get_AuthorDAO()

        author_dao.remove(item)

        self.listbox.delete(selection)

    def delete_publisher(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)

        publisher_dao = self.dao_factory.get_PublisherDAO()

        publisher_dao.remove(item)

        self.listbox.delete(selection)

    def delete_user(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)

        user_dao = self.dao_factory.get_UserDAO()

        user_dao.remove(item)

        self.listbox.delete(selection)

    def delete_book(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)

        book_dao = self.dao_factory.get_BookDAO()

        book_dao.remove(item)

        self.listbox.delete(selection)

    def delete_copy(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)

        digits = []
        for s in item.split():
            if s.isdigit():
                digits.append(s)

        id = int(digits[0])
        copy_dao = self.dao_factory.get_CopyDAO()

        copy = copy_dao.get(id)

        copy_dao.remove(copy)

        self.listbox.delete(selection)

    def delete_loan(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)
        digits = []
        for s in item.split():
            if s.isdigit():
                digits.append(s)

        id = int(digits[0])

        loan_dao = self.dao_factory.get_LoanDAO()
        loan = loan_dao.get_from_copy_id(id)

        loan_dao.remove(loan)
        print(item)

        self.listbox.delete(selection)

    #EDIT FUNCTIONS

    def edit(self):
        selection = self.listbox.curselection()
        item = self.listbox.get(selection)

        if self.current_view == views.AUTHORS:
            self.edit_author(item)
        elif self.current_view == views.PUBLISHERS:
            self.edit_publisher(item)
        elif self.current_view == views.USERS:
            self.edit_user(item)
        elif self.current_view == views.BOOKS:
            self.edit_book(item)
        elif self.current_view == views.COPIES:
            self.edit_copy(item)
        else:
            self.edit_loan(item)

    def edit_author(self, item):
        author_dao = self.dao_factory.get_AuthorDAO()
        author = author_dao.get_from_name(item)
        Edit_author_window(self.master, self.dao_factory, author)

    def edit_publisher(self, item):
        publisher_dao = self.dao_factory.get_PublisherDAO()
        publisher = publisher_dao.get_from_name(item)
        Edit_publisher_window(self.master, self.dao_factory, publisher)

    def edit_user(self, item):
        user_dao = self.dao_factory.get_UserDAO()
        user = user_dao.get_from_name(item)
        Edit_user_window(self.master, self.dao_factory, user)

    def edit_book(self, item):
        book_dao = self.dao_factory.get_BookDAO()
        book = book_dao.get_from_name(item)
        Edit_book_window(self.master, self.dao_factory, book)

    def edit_copy(self, item):
        digits = []
        for s in item.split():
            if s.isdigit():
                digits.append(s)

        id = int(digits[0])
        copy_dao = self.dao_factory.get_CopyDAO()

        copy = copy_dao.get(id)

        Edit_copy_window(self.master, self.dao_factory, copy)

    def edit_loan(self, item):
        digits = []
        for s in item.split():
            if s.isdigit():
                digits.append(s)

        id = int(digits[0])

        loan_dao = self.dao_factory.get_LoanDAO()
        loan = loan_dao.get_from_copy_id(id)

        Edit_loan_window(self.master, self.dao_factory, loan)


    #other functions
    def update(self):
        view = self.current_view
        self.current_view = views.NONE

        selection = self.listbox.curselection()

        if view == views.AUTHORS:
            self.show_authors()
        elif view == views.PUBLISHERS:
            self.show_publishers()
        elif view == views.USERS:
            self.show_users()
        elif view == views.BOOKS:
            self.show_books()
        elif view == views.COPIES:
            self.show_copies()
        else:
            self.show_loans()

        if selection:
            self.listbox.select_set(selection[0])
