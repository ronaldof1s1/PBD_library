from Control.DAOs import *
from Model.Models import *
import psycopg2

conn = psycopg2.connect("dbname='PBD_library' user='postgres' password='postgres'")
cursor = conn.cursor()

AuthorDAO(cursor).create_table()
PublisherDAO(cursor).create_table()
LibraryUserDAO(cursor).create_table()
BookDAO(cursor).create_table()
CopyDAO(cursor).create_table()
LoanDAO(cursor).create_table()

conn.commit()

cursor.close()
conn.close()