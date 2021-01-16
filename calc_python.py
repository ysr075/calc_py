def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

while True:
    choose = float(input("\n1.plus or 2.minus or 3.divide or 4.multiply: "))
    if choose == 1:
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        print("\n")
        print(num1, "+", num2, "=", add(num1, num2))
    elif choose == 2:
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        print("\n")
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choose == 3:
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        print("\n")
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choose == 4:
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        print("\n")
        print(num1, "*", num2, "=", multiply(num1, num2))
    else:
        exit()
