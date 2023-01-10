import math

digit = input()

def toFixed(digits):
    return f"{math.pi:.{digits}f}"

print(toFixed(digit))