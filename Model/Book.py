class Book:

    def __init__(self, name, keywords, publisher):
        self.name = name
        self.keywords = keywords
        self.publisher = publisher

    def __str__(self):
        return self.name