class User:

    def __init__(self, name, address, telephone, student):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.student = student

    def __str__(self):
        return self.name