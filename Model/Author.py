class Author:

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return self.name