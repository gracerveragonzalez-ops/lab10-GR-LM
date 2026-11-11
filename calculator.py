<<<<<<< HEAD
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
=======
import math


def square_root(a):
   try:
       if a<0:
           raise ValueError
       return math.sqrt(a)
   except ValueError:
       raise


def hypotenuse(a, b):
   try:
       return math.hypot(a, b)
   except ValueError:
       raise




def add(a, b):
   return a + b


def subtract(a, b):
   return a - b




def multiply(a, b):
   return a * b




def divide(a, b):
   if a == 0:
       raise ZeroDivisionError
   return b / a




def logarithm(a, b):
   if a <= 0 or a == 1 or b <= 0:
       raise ValueError
   return math.log(b, a)




def exponent(a, b):
   return a ** b
>>>>>>> 465f0620b45e80ff6e7d553b044d9b804fb6ab31


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)


def exp(a, b):
    return a ** b