from account import *
from transaction import *
from budget import *
from datetime import datetime

# takes a dict of transactions and their amounts
def find_categories_amount(transactions):
    category_costs = {}
    for trans in transactions:
        category_costs[trans.category] = trans.amount
    return category_costs

# def category_ratio(category_cost):
#     total = 0
    


if __name__ == "__main__":
    free_checking = Account("Free Checking", "checking", 1000)
    free_checking.deposit(125)

    my_budget = Budget(1000)
    my_budget.addIncome(500, "Pay Check", datetime(2025,4,10))
    my_budget.addExpense(100, "Groceries", datetime(2025, 4, 10))
    my_budget.addExpense(30, "Recreation", datetime(2025, 4, 5))
    my_budget.addExpense(500, "Rent", datetime(2025, 4, 1))
    my_budget.addExpense(30, "Gas", datetime(2025, 4, 8))
    my_budget.addExpense(24, "Eating out", datetime(2025, 4, 9))
    my_budget.addExpense(10, "Eating out", datetime(2025, 4, 7))
    my_budget.addExpense(80, "Eating out", datetime(2025, 4, 8))

    # my_budget.plotExpenses()
    my_budget.pieExpences()

    # print(free_checking)
    # trans1 = Transaction("Walmart", 200, free_checking, "Groceries", "hahaha")
    # trans2 = Transaction("Peak Nights", 30, free_checking, "Recreational", "hahaha")
    # print(trans1)
    # print(find_categories_amount([trans1, trans2]))