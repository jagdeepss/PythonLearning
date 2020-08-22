"""
This contains the basics of Functions
"""

# ------------------------------------- FUNCTION WITH DEFAULT VALUES ----------------------------------


def fun_with_default_values(x=6, y=7):
    """Function with default Value"""
    print(" x+y = ", x+y)


#  Driver code to test above method
fun_with_default_values()
fun_with_default_values(9, 12)
fun_with_default_values(y=12)  # Passing Single Value


# ------------------------------------- FUNCTION WITH ARBITRARY VALUES ----------------------------------

"""
This is used when we do not know in advance the number of arguments that will be passed to the function
"""
def fun_with_arbitrary_value(*args):
    """Function accepts the arbitrary values"""
    for argValue in args:
        print("Argument value is : ", args)
    return sum(args)


#  Driver code to test above method
abrListArgs = (2, 3, 4, 5, 6)
print("Sum of arbitrary values: ", fun_with_arbitrary_value(*abrListArgs))


# ------------------------------------- FUNCTION WITH ARBITRARY KEY VALUES PAIRS----------------------------------

"""
This is used when we do not know in advance the number of arguments that will be passed to the function
"""


def fun_with_arbitrary_key_value(**args):
    """Function accepts the arbitrary values"""
    for argKey, argValue in args.items():
        print("Argument value is : ", argKey, "  Argument value is : ", argValue)
    return sum(args.values())


#  Driver code to test above method
studentMathGrades = {"kim" : 12, "jay" : 15, "jass" : 30}
print("Sum of arbitrary values: ", fun_with_arbitrary_key_value(**studentMathGrades))
