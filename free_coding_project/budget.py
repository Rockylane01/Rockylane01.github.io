
import matplotlib.pyplot as plt

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

        if self.transaction_history["income_value"] == []:
            self.transaction_history['income_value'].append(income)
            self.transaction_history['income_category'].append(category)
            self.transaction_history['income_date'].append(date)
        else:
            for i in range(len(list(self.transaction_history.values())[0])):
                if self.transaction_history['income_date'][i] > date:
                    self.transaction_history['income_value'].insert(i, income)
                    self.transaction_history['income_category'].insert(i, category)
                    self.transaction_history['income_date'].insert(i, date)

        # print(self.transaction_history)
        # print(self.balance)


    def addExpense(self, expense, category, date):
        self.balance -= expense

        if self.transaction_history["expense_value"] == []:
            self.transaction_history['expense_value'].append(expense)
            self.transaction_history['expense_category'].append(category)
            self.transaction_history['expense_date'].append(date)
        else:
            for i in range(len(self.transaction_history['expense_date'])):
                if self.transaction_history['expense_date'][i] >= date:
                    self.transaction_history['expense_value'].insert(i, expense)
                    self.transaction_history['expense_category'].insert(i, category)
                    self.transaction_history['expense_date'].insert(i, date)
                    break

        # print([x.day for x in self.transaction_history['expense_date']])
        # print(self.balance)

    def plotExpenses(self):
        X = [x.day for x in self.transaction_history['expense_date']]
        Y = self.transaction_history['expense_value']
        print(X, Y)

        plt.plot(X, Y)
        plt.xlabel('Day of month')
        plt.ylabel('Expense amount in USD')
        plt.title('Expense overview')
        plt.savefig("data_vis/expense_plot.png")

    def pieExpences(self):
        cat_values = {}
        # sum_expenses = {}
        total_expense = 0
        # cat_perc = {}
        categories = []
        cat_perc = []
        
        print(self.transaction_history['expense_category'])
        for i in range(len(self.transaction_history['expense_category'])):
            category = self.transaction_history['expense_category'][i]
            expense = self.transaction_history['expense_value'][i]
            if category in cat_values:
                cat_values[category].append(expense)
            else:
                cat_values[category] = [expense]
        
        for key in cat_values:
            total_expense += sum(cat_values[key])
            # cat_perc[key] = int((sum(cat_values[key]) / total_expense) * 100)

        for key in cat_values:
            categories.append(key)
            cat_perc.append((sum(cat_values[key]) / total_expense) * 100)
        
        plt.pie(cat_perc, labels=categories)
        plt.savefig("data_vis/expense_pie.png")

    def plotExpenseDistribution(self):
        pass
