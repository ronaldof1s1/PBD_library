class LoanDAO:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        self.db.execute("CREATE TABLE loan (id SERIAL PRIMARY KEY, loan_date DATE NOT NULL, return_date DATE, copy_id INTEGER NOT NULL REFERENCES copy (id), user_id INTEGER NOT NULL REFERENCES user (id) )")