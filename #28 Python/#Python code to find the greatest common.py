#Python code to find the greatest common divisor (GCD) of two numbers using recursion:
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)