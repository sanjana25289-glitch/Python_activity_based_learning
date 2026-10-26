
income = int(input("Enter monthly income: "))
rent = int(input("Enter rent expenses: "))
food = int(input("Enter food expenses: "))
travel = int(input("Enter travel expenses: "))

total = rent + food + travel
savings = income - total

print("Monthly Income:", income)
print("Rent Expenses:", rent)
print("Food Expenses:", food)
print("Travel Expenses:", travel)
print("Total Expenses:", total)
print("Savings:", savings)
