class Account:
    def __init__(self, name, type, balance=0):
        self.name = name
        self.type = type
        self.balance = balance

    def __str__(self):
        return f"Account: {self.name}\nType: {self.type}\nBalance: {self.balance}"

    def __repr__(self):
        return f"Account({self.name}, {self.type}, {self.balance})"

    def deposit(self, dep):
        self.balance += dep

    def withdraw(self, cost):
        self.balance -= cost

# if __name__ == "__main__":
#     free_checking = Account("Free Checking", "checking", 300)
#     free_checking.withdraw(125)
#     print(free_checking)
