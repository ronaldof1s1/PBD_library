class Book:

    def __init__(self, name, keywords, publisher, author):
        self.name = name
        self.keywords = keywords
        self.publisher = publisher
        self.author = author

    def __str__(self):
        return self.name