#Example of a try-except block that handles a ZeroDivisionErro
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero.")