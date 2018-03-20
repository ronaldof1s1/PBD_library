class Copy:

    def __init__(self, lent, quantity, book):
        self.lent = lent
        self.quantity = quantity
        self.book = book

    def __str__(self):
        return self.book.name + " exemplar"