# ------Continue will skip next steps Statement so 5 will be skipped --------
"""
break, continue, pass in Python

break – takes you out of the current loop.

continue – ends the current iteration in the loop and moves to the next iteration.

pass – The pass statement does nothing. It can be used when a statement is required.
syntactically but the program requires no action. It is commonly used for creating minimal classes.
"""

print("This is continue example")
for numb in range(10):
    """ The is continue example will skip the print of 5 """

    if numb == 5:
        continue
    print(numb, end=',')

print("This is pass example")
for numb in range(10):
    """ The is pass example will does nothing for the print of 5"""

    if numb == 5:
        pass
    print(numb, end=',')

print("This is break example")
for numb in range(10):
    """ The is break example will does exit after 4"""

    if numb == 5:
        break
    print(numb, end=',')