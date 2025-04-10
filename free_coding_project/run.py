from account import *
from transaction import *

# takes a dict of transactions and their amounts
def find_categories_amount(transactions):
    category_costs = {}
    for trans in transactions:
        category_costs[trans.category] = trans.amount
    return category_costs

# def category_ratio(category_cost):
#     total = 0
    


if __name__ == "__main__":
    free_checking = Account("Free Checking", "checking", 300)
    free_checking.withdraw(125)
    # print(free_checking)
    trans1 = Transaction("Walmart", 200, free_checking, "Groceries", "hahaha")
    trans2 = Transaction("Peak Nights", 30, free_checking, "Recreational", "hahaha")
    print(trans1)
    print(find_categories_amount([trans1, trans2]))