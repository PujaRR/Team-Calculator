# advanced.py
import math
def sqrt(x):
    if x < 0:
        raise ValueError("sqrt of negative")
    return math.sqrt(x)

def power(a, b):
    return a ** b

def percentage(part, whole):
    if whole == 0:
        raise ValueError("whole cannot be zero")
    return (part / whole) * 100
