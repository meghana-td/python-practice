def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1 to 4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid! Enter choice between 1 and 4")
        continue

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print(n1, "+", n2, "=", add(n1, n2))
    elif choice == '2':
        print(n1, "-", n2, "=", subtract(n1, n2))
    elif choice == '3':
        print(n1, "*", n2, "=", multiply(n1, n2))
    elif choice == '4':
        if n2==0:
            print ("Division by zero not possible ")
        else:
            print(n1, "/", n2, "=", divide(n1, n2))

    next_calculation = input("Let's do next calculation? (yes/no): ")

    if next_calculation.lower() == "no":
        break
