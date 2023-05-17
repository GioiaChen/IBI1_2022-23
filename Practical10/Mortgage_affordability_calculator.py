def calculate(x, y):
    if x > y*5:
        print("NO! Save more money for buying a house please.")
    else:
        print("Yes")


price = input("Price = ")
salary = input("Salary = ")
calculate(price, salary)
