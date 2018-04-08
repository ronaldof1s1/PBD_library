from Model.Models import *
from ConfigReader import ConfigReader

cr = ConfigReader("configfile.json")

db = cr.get_DB()
uri = cr.get_uri()

if db == "Postgresql" :
    import psycopg2
    from Control.PostgresqlDAOs import *

    conn = psycopg2.connect(uri)
    cursor = conn.cursor()
    cursor.close()

elif db == "MongoDB":
    import pymongo
    from Control.MongoDAOs import *

    conn = pymongo.MongoClient(uri)



conn.close()