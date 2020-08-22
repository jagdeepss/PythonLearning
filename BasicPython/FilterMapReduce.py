"""
This is for 3 Functions in Python
1. Filter
2. Map
3. Reduce

Filter and Map are lazy functions. Both are higher order functions.
Functions in python are objects like types and can be assigned to variables, passed to functions
and returned from functions. One can pass named functions. In case you are not not using named functions
need to use lambdas.
"""
import math

numList = [10, 20, 30, 40, 50]


def is_grater_than_30(x):
    return x > 30


def get_square(x):
    return x ** 2

# ------------- Using Named Function For Filter -------------
output = list(filter(is_grater_than_30, numList))
print(output)  # [40, 50]

# ------------ Using Lambda for Filter ----------------------
output1 = list(filter(lambda x: x > 30, numList))
print(output1)  # [40, 50]


# ------------- Using Named Function for Map -------------
output3 = list(map(get_square, numList))
print(output3)  # [100, 400, 900, 1600, 2500]

# ------------ Using Lambda for Map ----------------------
output4 = list(map(lambda x: x ** 2, numList))
print(output4)  # [100, 400, 900, 1600, 2500]

# ------------ Using map and filter
output5 = list(map(lambda x: x ** 2, filter(lambda x: x > 30, numList)))
print(output5)  # [1600, 2500]

# Alternate to Map
reversed_number = [num ** 2 for num in reversed(output1)]
print(reversed_number)  # [2500, 1600]



