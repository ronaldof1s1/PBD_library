from Control.DAOs import *
import psycopg2

conn = psycopg2.connect("dbname='PBD_library' user='postgres' password='postgres'")
cursor = conn.cursor()


cursor.close()
conn.close()