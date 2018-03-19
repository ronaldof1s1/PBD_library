class Loan:

    def __init__(self, loan_date, return_date, copy, user):
        self.loan_date = loan_date
        self.return_date = return_date
        self.copy = copy
        self.user = user

    def __str__(self):
        return self.copy + " -> " + self.user


