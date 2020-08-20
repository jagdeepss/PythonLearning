"""
This contains the basics of Functions
"""


def fun_with_default_values(x=6, y=7):
    """Function with default Value"""
    print(" x+y = ", x+y)


# Test the fun_with_default_values
fun_with_default_values()
fun_with_default_values(9, 12)
fun_with_default_values(y=12)  # Passing Single Value


"""
This is used when we do not know in advance the number of arguments that will be passed to the function
"""


def fun_with_arbitary_value(*args):
    """Function accepts the arbitary values"""
    for argValue in args:
        print("Argument valie is : ",args)
    return sum(args)


# Test the fun_with_arbitary_value
print("Sum of arbitrary values: ", fun_with_arbitary_value(2,3,4,5,6))

