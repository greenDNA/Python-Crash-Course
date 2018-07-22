print("Enter two numbers")
try:
    number1 = int(input("> "))
    number2 = int(input("> "))
except Exception:
    print("Incorrect input. Numbers please.")
else:
    print(number1 + number2)
