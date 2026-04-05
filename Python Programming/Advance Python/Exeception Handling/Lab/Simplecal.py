try:
    a = float(input("Enter a value of a: "))
    b = float(input("Enter a value of b: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Addition :", a + b)
    elif operator == "-":
        print("Substraction :", a - b)
    elif operator == "*":
        print("Multiplication:", a * b)
    elif operator == "/":
        print("Division:", a / b)
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("Error: divide by zero error")

except ValueError:
    print("Error: Invalid input error")