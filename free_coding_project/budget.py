class Budget:

    # Keeps track of the pas transaction so you can plot it later
    transaction_history = {
        'income_value':[],
        'income_category':[],
        'income_date':[],
        'expense_value':[],
        'expense_category':[],
        'expense_date':[],
    }

    def __init__(self, balance):
        self.balance = balance

    def addIncome(self, income, category, date):
        self.balance += income

        self.transaction_history['income_value'].append(income)
        self.transaction_history['income_category'].append(category)
        self.transaction_history['income_date'].append(date)

    def addExpense(self, expense, category, date):
        self.balance -= expense

        self.transaction_history['expense_value'].append(expense)
        self.transaction_history['expense_category'].append(category)
        self.transaction_history['expense_date'].append(date)

    def plotExpenses(self):
        pass

    def plotExpenseDistribution(self):
        pass
