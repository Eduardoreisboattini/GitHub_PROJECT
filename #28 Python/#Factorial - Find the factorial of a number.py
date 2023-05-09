#Python code to find the factorial of a number using recursion:act.js 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)