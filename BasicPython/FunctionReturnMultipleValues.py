"""In Python Function return one value. If multiple
values needs to be return then
Examples are from https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
"""

# ---------------------------- OPTION 1 ---------------------------------
"""
Using Object: This is similar to C/C++ and Java, we can create a class (in C, struct) 
to hold multiple values and return an object of the class.
"""


class Test:
    def __init__(self):
        self.str = "geeksforgeeks"
        self.x = 20


def return_object():
    """This function returns an object of Test"""
    return Test()


# Driver code to test above method
t = return_object()
print(t.str)
print(t.x)


# ---------------------------- OPTION 2 ---------------------------------
"""
Using Tuple: A Tuple is a comma separated sequence of items. 
It is created with or without (). 
IMPORTANT NOTE : Tuples are immutable. 
"""


def return_tuple():
    """This function returns a tuple"""
    str1 = "geeksforgeeks"
    x1 = 20
    return str1, x1  # Return tuple, we could also write (str, x)


# Driver code to test above method
strVal, xVal = return_tuple()  # Assign returned tuple
print("strVal ", strVal, " xVal ", xVal)


# ---------------------------- OPTION 3 ---------------------------------

"""
Using a list: A list is like an array of items created using square brackets. 
They are different from arrays as they can contain items of different types. 
IMPORTANT NOTE : Lists are different from tuples as they are mutable.
"""


def return_list():
    """This function returns a tuple"""
    str1 = "geeksforgeeks"
    x1 = 20
    return [str1, x1]


# Driver code to test above method
listVal = return_list()
print("listVal ", listVal)


# ---------------------------- OPTION 4 ---------------------------------
"""
Using a Dictionary: A Dictionary is similar to hash or map in other languages. 
It consists of key value pairs. The value can be accessed by unique key in the dictionary.
"""


def return_dict():
    d = dict()  # Declaring the dictionary
    d['str'] = "GeeksForGeeks"
    d['x'] = 20
    return d


# Driver code to test above method
dictVal = return_dict()
print("dictVal ", dictVal)
print("dictVal x ", dictVal['x'], " dictVal str ", dictVal['str'])


