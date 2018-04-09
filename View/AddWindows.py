from tkinter import *
from sys import path
path.append("..")
from Model.Models import *
from .MainWindow import *
from datetime import date, datetime

class Add_author_window:
    def __init__(self, master, dao_factory):
        self.master = master
        self.dao_factory = dao_factory

        self.top = Toplevel(master)
        self.top.title("ADD AUTHOR")

        #WIDGETS

        self.label_frame = Frame(self.top)
        self.entry_frame = Frame(self.top)
        self.button_frame = Frame(self.top)

        self.name_label = Label(self.label_frame,text="name")
        self.address_label = Label(self.label_frame, text="address")
        self.telephone_label = Label(self.label_frame, text="telephone")

        self.name_entry = Entry(self.entry_frame)
        self.address_entry = Entry(self.entry_frame)
        self.telephone_entry = Entry(self.entry_frame)

        self.add_button = Button(self.button_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.cancel_button = Button(self.button_frame, text="cancel", bg="RED", command=self.quit)
        self.no_button = Frame(self.button_frame)

        #LAYOUT

        self.name_label.grid(row=0, column=0, sticky=E)
        self.address_label.grid(row=1, column=0, sticky=E)
        self.telephone_label.grid(row=2, column=0, sticky=E)

        self.label_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.name_entry.grid(row=0, column=0, sticky=E+W+N+S)
        self.address_entry.grid(row=1, column=0, sticky=E+W+N+S)
        self.telephone_entry.grid(row=2, column=0, sticky=E+W+N+S)

        self.entry_frame.grid(row = 0, column=1, sticky=E+W+N+S)

        self.add_button.grid(row=0, column=0, sticky=E+W+N+S, ipadx=20)
        self.no_button.grid(row=0, column=1, ipadx=30)
        self.cancel_button.grid(row=0, column=2, sticky=E+W+N+S, ipadx=20)

        self.button_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

    def add(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        telephone = self.telephone_entry.get()

        # print(telephone)
        author = Author(name, address, telephone)
        print(author)
        author_dao = self.dao_factory.get_AuthorDAO()
        author_dao.insert(author)
        self.quit()

    def quit(self):
        self.top.destroy()

class Add_publisher_window:
    def __init__(self, master, dao_factory):
        self.master = master
        self.dao_factory = dao_factory

        self.top = Toplevel(master)
        self.top.title("ADD PUBLISHER")

        #WIDGETS

        self.label_frame = Frame(self.top)
        self.entry_frame = Frame(self.top)
        self.button_frame = Frame(self.top)

        self.name_label = Label(self.label_frame,text="name")
        self.address_label = Label(self.label_frame, text="address")
        self.telephone_label = Label(self.label_frame, text="telephone")

        self.name_entry = Entry(self.entry_frame)
        self.address_entry = Entry(self.entry_frame)
        self.telephone_entry = Entry(self.entry_frame)

        self.add_button = Button(self.button_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.cancel_button = Button(self.button_frame, text="cancel", bg="RED", command=self.quit)
        self.no_button = Frame(self.button_frame)

        #LAYOUT

        self.name_label.grid(row=0, column=0, sticky=E)
        self.address_label.grid(row=1, column=0, sticky=E)
        self.telephone_label.grid(row=2, column=0, sticky=E)

        self.label_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.name_entry.grid(row=0, column=0, sticky=E+W+N+S)
        self.address_entry.grid(row=1, column=0, sticky=E+W+N+S)
        self.telephone_entry.grid(row=2, column=0, sticky=E+W+N+S)

        self.entry_frame.grid(row = 0, column=1, sticky=E+W+N+S)

        self.add_button.grid(row=0, column=0, sticky=E+W+N+S, ipadx=20)
        self.no_button.grid(row=0, column=1, ipadx=30)
        self.cancel_button.grid(row=0, column=2, sticky=E+W+N+S, ipadx=20)

        self.button_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

    def add(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        telephone = self.telephone_entry.get()

        # print(telephone)
        publisher = Publisher(name, address, telephone)
        print(publisher)
        publisher_dao = self.dao_factory.get_PublisherDAO()
        publisher_dao.insert(publisher)
        self.quit()

    def quit(self):
        self.top.destroy()

class Add_user_window:
    def __init__(self, master, dao_factory):
        self.master = master
        self.dao_factory = dao_factory

        self.top = Toplevel(master)
        self.top.title("ADD USER")

        #WIDGETS

        self.label_frame = Frame(self.top)
        self.entry_frame = Frame(self.top)
        self.button_frame = Frame(self.top)

        self.name_label = Label(self.label_frame,text="name")
        self.address_label = Label(self.label_frame, text="address")
        self.telephone_label = Label(self.label_frame, text="telephone")
        self.student_label = Label(self.label_frame, text="student")

        self.student = BooleanVar()

        self.name_entry = Entry(self.entry_frame)
        self.address_entry = Entry(self.entry_frame)
        self.telephone_entry = Entry(self.entry_frame)
        self.student_check = Checkbutton(self.entry_frame, variable=self.student)

        self.add_button = Button(self.button_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.cancel_button = Button(self.button_frame, text="cancel", bg="RED", command=self.quit)
        self.no_button = Frame(self.button_frame)

        #LAYOUT

        self.name_label.grid(row=0, column=0, sticky=E)
        self.address_label.grid(row=1, column=0, sticky=E)
        self.telephone_label.grid(row=2, column=0, sticky=E)
        self.student_label.grid(row=3, column=0, sticky=E)

        self.label_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.name_entry.grid(row=0, column=0, sticky=E+W+N+S)
        self.address_entry.grid(row=1, column=0, sticky=E+W+N+S)
        self.telephone_entry.grid(row=2, column=0, sticky=E+W+N+S)
        self.student_check.grid(row=3, column=0, sticky=E+W+N+S)

        self.entry_frame.grid(row = 0, column=1, sticky=E+W+N+S)

        self.add_button.grid(row=0, column=0, sticky=E+W+N+S, ipadx=20)
        self.no_button.grid(row=0, column=1, ipadx=30)
        self.cancel_button.grid(row=0, column=2, sticky=E+W+N+S, ipadx=20)

        self.button_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

    def add(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        telephone = self.telephone_entry.get()
        student = self.student.get()

        print(student)
        user = LibraryUser(name, address, telephone, student)
        student_dao = self.dao_factory.get_UserDAO()
        student_dao.insert(user)
        self.quit()

    def quit(self):
        self.top.destroy()

class Add_book_window:
    def __init__(self, master, dao_factory):
        self.master = master
        self.dao_factory = dao_factory

        self.top = Toplevel(master)
        self.top.title("ADD BOOK")

        #WIDGETS

        self.label_frame = Frame(self.top)
        self.entry_frame = Frame(self.top)
        self.button_frame = Frame(self.top)

        self.name_label = Label(self.label_frame,text="name")
        self.keywords_label = Label(self.label_frame, text="keywords")
        self.quantity_label = Label(self.label_frame, text="quantity")
        self.publisher_label = Label(self.label_frame, text="publisher")
        self.author_label = Label(self.label_frame, text="author")

        self.publisher_name = StringVar()
        self.author_name = StringVar()

        self.name_entry = Entry(self.entry_frame)
        self.keywords_entry = Entry(self.entry_frame)
        self.quantity_entry = Entry(self.entry_frame)
        self.publisher_drop_down = OptionMenu(self.entry_frame, self.publisher_name, *(self.get_publishers()))
        self.author_drop_down = OptionMenu(self.entry_frame, self.author_name, *(self.get_authors()))

        self.add_button = Button(self.button_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.cancel_button = Button(self.button_frame, text="cancel", bg="RED", command=self.quit)
        self.no_button = Frame(self.button_frame)

        #LAYOUT

        self.name_label.grid(row=0, column=0, sticky=E)
        self.keywords_label.grid(row=1, column=0, sticky=E)
        self.quantity_label.grid(row=2, column=0, sticky=E)
        self.publisher_label.grid(row=3, column=0, sticky=E)
        self.author_label.grid(row=4, column=0, sticky=E)


        self.label_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.name_entry.grid(row=0, column=0, sticky=E+W+N+S)
        self.keywords_entry.grid(row=1, column=0, sticky=E+W+N+S)
        self.quantity_entry.grid(row=2, column=0, sticky=E+W+N+S)
        self.publisher_drop_down.grid(row=3, column=0, sticky=E+W+N+S)
        self.author_drop_down.grid(row=4, column=0, sticky=E+W+N+S)

        self.entry_frame.grid(row = 0, column=1, sticky=E+W+N+S)

        self.add_button.grid(row=0, column=0, sticky=E+W+N+S, ipadx=20)
        self.no_button.grid(row=0, column=1, ipadx=30)
        self.cancel_button.grid(row=0, column=2, sticky=E+W+N+S, ipadx=20)

        self.button_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

    def add(self):
        name = self.name_entry.get()
        keywords_all = self.keywords_entry.get()
        quantity = int(self.quantity_entry.get())


        keywords = keywords_all.split(",")
        for word in keywords:
            word = word.strip()

        author = self.dao_factory.get_AuthorDAO().get_from_name(self.author_name.get())
        publisher = self.dao_factory.get_PublisherDAO().get_from_name(self.publisher_name.get())


        book = Book(name, keywords, quantity, publisher, author)
        print (book.quantity)

        book_dao = self.dao_factory.get_BookDAO()
        book_dao.insert(book)
        self.quit()

    def quit(self):
        self.top.destroy()

    def get_authors(self):
        author_dao = self.dao_factory.get_AuthorDAO()
        authors = author_dao.get_all()
        return authors

    def get_publishers(self):
        publisher_dao = self.dao_factory.get_PublisherDAO()
        publishers = publisher_dao.get_all()
        return publishers

class Add_copy_window:
    def __init__(self, master, dao_factory):
        self.master = master
        self.dao_factory = dao_factory

        self.top = Toplevel(master)
        self.top.title("ADD COPY")

        #WIDGETS

        self.label_frame = Frame(self.top)
        self.entry_frame = Frame(self.top)
        self.button_frame = Frame(self.top)

        self.id_label = Label(self.label_frame,text="id")
        self.book_label = Label(self.label_frame, text="book")
        self.lent_label = Label(self.label_frame, text="lent")

        self.lent = BooleanVar()
        self.book_name = StringVar()

        self.id_entry = Entry(self.entry_frame)
        self.book_drop_down = OptionMenu(self.entry_frame, self.book_name, *(self.get_books()))
        self.lent_checkbox = Checkbutton(self.entry_frame, variable=self.lent)

        self.add_button = Button(self.button_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.cancel_button = Button(self.button_frame, text="cancel", bg="RED", command=self.quit)
        self.no_button = Frame(self.button_frame)

        #LAYOUT

        self.id_label.grid(row=0, column=0, sticky=E)
        self.book_label.grid(row=1, column=0, sticky=E)
        self.lent_label.grid(row=2, column=0, sticky=E)

        self.label_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.id_entry.grid(row=0, column=0, sticky=E+W+N+S)
        self.book_drop_down.grid(row=1, column=0, sticky=E+W+N+S)
        self.lent_checkbox.grid(row=2, column=0, sticky=E+W+N+S)

        self.entry_frame.grid(row = 0, column=1, sticky=E+W+N+S)

        self.add_button.grid(row=0, column=0, sticky=E+W+N+S, ipadx=20)
        self.no_button.grid(row=0, column=1, ipadx=30)
        self.cancel_button.grid(row=0, column=2, sticky=E+W+N+S, ipadx=20)

        self.button_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

    def add(self):
        id = int(self.id_entry.get())
        book_name = self.book_name.get()
        lent = self.lent.get()

        book = self.dao_factory.get_BookDAO().get_from_name(book_name)

        copy = Copy(id, lent, book)

        copy_dao = self.dao_factory.get_CopyDAO()
        copy_dao.insert(copy)
        self.quit()

    def quit(self):
        self.top.destroy()

    def get_books(self):
        book_dao = self.dao_factory.get_BookDAO()
        books = book_dao.get_all()
        return books

class Add_loan_window:
    def __init__(self, master, dao_factory):
        self.master = master
        self.dao_factory = dao_factory

        self.top = Toplevel(master)
        self.top.title("ADD LOAN")

        #WIDGETS

        self.label_frame = Frame(self.top)
        self.entry_frame = Frame(self.top)
        self.button_frame = Frame(self.top)

        self.loan_date_label = Label(self.label_frame,text="Loan date")
        self.return_date_label = Label(self.label_frame, text="Return date")
        self.copy_label = Label(self.label_frame, text="Copy")
        self.user_label = Label(self.label_frame, text="User")

        self.copy_name = StringVar()
        self.user_name = StringVar()

        self.loan_date_entry = Entry(self.entry_frame)
        self.return_date_entry = Entry(self.entry_frame)
        self.copy_drop_down = OptionMenu(self.entry_frame, self.copy_name, *(self.get_copies()))
        self.user_drop_down = OptionMenu(self.entry_frame, self.user_name, *(self.get_users()))


        self.add_button = Button(self.button_frame, text="ADD", bg="LIGHTGREEN", command=self.add)
        self.cancel_button = Button(self.button_frame, text="cancel", bg="RED", command=self.quit)
        self.no_button = Frame(self.button_frame)

        #LAYOUT

        self.loan_date_label.grid(row=0, column=0, sticky=E)
        self.return_date_label.grid(row=1, column=0, sticky=E)
        self.copy_label.grid(row=2, column=0, sticky=E)
        self.user_label.grid(row=3, column=0, sticky=E)

        self.label_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.loan_date_entry.grid(row=0, column=0, sticky=E+W+N+S)
        self.return_date_entry.grid(row=1, column=0, sticky=E+W+N+S)
        self.copy_drop_down.grid(row=2, column=0, sticky=E+W+N+S)
        self.user_drop_down.grid(row=3, column=0, sticky=E+W+N+S)

        self.entry_frame.grid(row = 0, column=1, sticky=E+W+N+S)

        self.add_button.grid(row=0, column=0, sticky=E+W+N+S, ipadx=20)
        self.no_button.grid(row=0, column=1, ipadx=30)
        self.cancel_button.grid(row=0, column=2, sticky=E+W+N+S, ipadx=20)

        self.button_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

    def add(self):
        loan_date_string = self.loan_date_entry.get()
        return_date_string = self.return_date_entry.get()

        loan_datetime = datetime.strptime(loan_date_string, "%d/%m/%Y")
        return_datetime = datetime.strptime(return_date_string, "%d/%m/%Y")

        copy_name = self.copy_name.get()
        copy_id = copy_name.split()[0]
        copy_id = int(copy_id)
        user_name = self.user_name.get()

        print(copy_id)

        user = self.dao_factory.get_UserDAO().get_from_name(user_name)
        copy = self.dao_factory.get_CopyDAO().get(copy_id)
        loan = Loan(copy, user, loan_datetime, return_datetime)

        loan_dao = self.dao_factory.get_LoanDAO()
        loan_dao.insert(loan)
        self.quit()

    def quit(self):
        self.top.destroy()

    def get_copies(self):
        copy_dao = self.dao_factory.get_CopyDAO()
        copies = copy_dao.get_all()
        return copies

    def get_users(self):
        users_dao = self.dao_factory.get_UserDAO()
        users = users_dao.get_all()
        return users