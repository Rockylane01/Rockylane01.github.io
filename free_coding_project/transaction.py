import datetime

class Transaction:
    def __init__(self, name, amount, account, category, memo="", date=datetime.datetime.now()):
        self.name = name
        self.amount = amount
        self.account = account
        self.category = category
        self.date = date
        self.memo = memo

    def __str__(self):
        return f"Name: {self.name}\nAmount: {self.amount}\nAccount: {self.account.name}\nCategory: {self.category}\nMemo: {self.memo}\nDate: {self.date}\n"

    def __repr__(self):
        return f"Transaction({self.name}, {self.amount}, {self.account.name}, {self.category}, {self.memo}, {self.date})"
