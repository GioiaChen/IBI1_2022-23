# Define a function to compare the price and salary.
def calculate(x, y):
    if x > y*5:
        print("NO! Save more money for buying a house!")
    else:
        print("Yes")

# Input the price and salary for comparison.
price = input("Price = ")
salary = input("Salary = ")

# Use the function.
calculate(price, salary)
