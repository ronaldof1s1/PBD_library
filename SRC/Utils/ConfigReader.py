import json

class ConfigReader():
    def __init__(self, file):
        self.data = json.load(open(file))

    def get_DB(self):
        db = self.data["database"]
        return db

    def get_uri(self):
        uri = self.data["uri"]
        return uri

