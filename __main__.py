from Control import *
from Model.Models import *
import psycopg2, pymongo

conn = psycopg2.connect("postgres://lirtwxkb:40HJuIQLBS9pWHGMGiSZbvSFfDpkFOBt@baasu.db.elephantsql.com:5432/lirtwxkb")
cursor = conn.cursor()



cursor.close()
conn.close()