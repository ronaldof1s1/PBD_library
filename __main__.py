from Model.Models import *
from ConfigReader import ConfigReader
from View.MainWindow import *
from DAOFactory import  DAOFactory
cr = ConfigReader("configfile.json")

db = cr.get_DB()
uri = cr.get_uri()

if db == "Postgresql" :
    import psycopg2

    conn = psycopg2.connect(uri)
    database = conn.cursor()

elif db == "MongoDB":
    import pymongo

    conn = pymongo.MongoClient()
    database = conn.PBDLIBRARY


dao_factory = DAOFactory(db, database)

root = Tk()
main_window = MainWindow(root, dao_factory)
root.mainloop()


conn.close()