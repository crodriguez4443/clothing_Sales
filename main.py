import math


def calculate_return(units):
    if percentage_sold < e_bird1_percent:
        income = round(percentage_sold * units) * e_bird1_price
        print("total income will be ${}".format(income))
    elif e_bird1_percent < percentage_sold <= e_bird2_percent:
        e_bird2_sold = units - e_bird1_quantity
        e_bird1_income = float(e_bird1_quantity * e_bird1_price)
        income = (e_bird2_sold * item_price) + e_bird1_income
        print("total income will be ${}".format(income))
    else:
        e_bird1_income = e_bird1_quantity * e_bird1_price
        e_bird2_income = e_bird2_quantity * e_bird2_price
        normal_sold = items_selling - e_bird1_quantity - e_bird2_quantity
        normal_income = normal_sold * normal_price
        income = e_bird1_income + e_bird2_income + normal_income
        print("total income will be ${}".format(income))
    return income


item_price = float(input("item price "))
items_ordered = int(input("items ordered "))
items_eaten = int(input("items eaten "))
items_selling = items_ordered - items_eaten
total_expense = items_selling * item_price

print("{} items are being sold".format(items_selling))
print("${} is the total expense needed to be recouped".format(total_expense))

e_bird1_price = input("what is the first early bird price? (20 for shirts) ")
e_bird2_price = input("what is the second early bird price? (22 for shirts) ")
normal_price = input("what is the normal price? (25 for shirts)")

e_bird1_percent = .15
e_bird2_percent = .5

e_bird1_quantity = math.ceil(e_bird1_percent * items_selling)
e_bird2_quantity = math.ceil(e_bird2_percent * items_selling)
normal_quantity = (items_selling - e_bird1_quantity - e_bird2_quantity)

print("{} early bird #1 items will be sold".format(e_bird1_quantity))
print("{} early bird #2 items will be sold".format(e_bird2_quantity))
print("{} normal price items will be sold".format(normal_quantity))

percentage_sold = float(input("what percentage of items are sold? "))

units_sold = percentage_sold * items_selling

net_income = calculate_return(units_sold)