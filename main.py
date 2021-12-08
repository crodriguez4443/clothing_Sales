import math

income = float(0)
item_price = float(input("item price "))
items_ordered = int(input("items ordered "))
total_expense = items_ordered * item_price

print(f"{items_ordered} items are being sold")
print(f"${total_expense} is the total expense to be recouped")

e_bird1_price = int(input("what is the first early bird price? (20 for shirts) "))
e_bird2_price = int(input("what is the second early bird price? (22 for shirts) "))
normal_price = int(input("what is the normal price? (25 for shirts)"))

e_bird1_percent = .15
e_bird2_percent = .5

e_bird1_quantity = math.ceil(e_bird1_percent * items_ordered)
e_bird2_quantity = math.ceil(e_bird2_percent * items_ordered)
normal_quantity = (items_ordered - e_bird1_quantity - e_bird2_quantity)

print(f"{e_bird1_quantity} early bird #1 items will be sold")
print(f"{e_bird2_quantity} early bird #2 items will be sold")
print(f"{normal_quantity} normal price items will be sold")

percentage_sold = float(input("what percentage of items are sold? "))

units_sold = percentage_sold * items_ordered

if units_sold <= e_bird1_quantity:
    income = float(units_sold * e_bird1_price)
    print(f"total income will be ${income}")
    if income < total_expense:
        difference = total_expense - income
        print(f"The difference is ${difference} in the RED.")
    elif income > total_expense:
        difference = income - total_expense
        print(f"The difference is ${difference} in the BLACK.")
    else:
        print("Wow, you broke completely even!")

elif e_bird1_quantity < units_sold <= e_bird2_quantity:
    income = float((e_bird1_quantity * e_bird1_price) + ((e_bird1_quantity + e_bird2_quantity - units_sold) * e_bird2_price))
    print(f"total income will be ${income}")
    if income < total_expense:
        difference = total_expense - income
        print(f"The difference is ${difference} in the RED.")
    elif income > total_expense:
        difference = income - total_expense
        print(f"The difference is ${difference} in the BLACK.")
    else:
        print("Wow, you broke completely even!")

elif e_bird2_quantity < units_sold:
    income = float((e_bird1_quantity * e_bird1_price) + (e_bird2_quantity * e_bird2_price) + ((e_bird1_quantity + e_bird2_quantity - units_sold) * normal_price))
    print(f"total income will be ${income}")
    def net_income(income):
        if income < total_expense:
            difference = total_expense - income
            print(f"The difference is ${difference} in the RED.")
        elif income > total_expense:
            difference = income - total_expense
            print(f"The difference is ${difference} in the BLACK.")
        else:
            print("Wow, you broke completely even!")
else:
    e_bird1_income = e_bird1_quantity * e_bird1_price
    e_bird2_income = e_bird2_quantity * e_bird2_price
    normal_sold = items_ordered - e_bird1_quantity - e_bird2_quantity
    normal_income = normal_sold * normal_price
    income = e_bird1_income + e_bird2_income + normal_income
    print(f"total income will be ${income}")
return income