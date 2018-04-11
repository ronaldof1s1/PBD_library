from View.MainWindow import *
from Utils.ConfigReader import *
from Utils.DAOFactory import *
import psycopg2, pymongo

class PBD_library:
    def __init__(self):

        self.cr = ConfigReader("configfile.json")

        self.db = self.cr.get_DB()
        self.uri = self.cr.get_uri()

        if self.db == "Postgresql" :

            self.conn = psycopg2.connect(dbname="PBD_library", user='postgres', password='postgres')
            conn.set_session(autocommit=True)
            self.database = self.conn.cursor()

        elif self.db == "MongoDB":

            self.conn = pymongo.MongoClient()
            self.database = self.conn.PBDLIBRARY


        self.dao_factory = DAOFactory(self.db, self.database)



        self.root = Tk()
        MainWindow(self.root, self.dao_factory)
        self.root.mainloop()



if __name__ == "__main__":
    pbd = PBD_library()
    pbd.conn.close()