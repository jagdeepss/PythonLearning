# -------------------------------------- LIST --------------------------------

"""
List
1. Its like array in other programming languages as contents can be accessed using index value.
But List is mutable as size can be increased
IMPORTANT NOTE : String and Tuple are immutable vs List is Mutable this is only and major difference
               : Tuple is created with () vs List is created with [] like arrays
               : Each item stored in a list or a tuple can be of any data
               : type e.g NumberListk = [20,  "30"], NumberTuple = (20, "30")
               : Tuple and List elements can be access by index number NumberListk[1], NumberTuple[1]

"""

NumberList = [20, 30, 40, 50]
print(NumberList[1], ", ", NumberList[0])  # 30, 20
"""
2. Negative number represent numbers from the last
"""
print(NumberList[-3], ", ", NumberList[-1])  # 30, 50 as it is counting in reverse

"""
3. Doing as sum based on Index
"""

print("Sum of 1 index and 3rd index ", NumberList[1 + 2])

"""
4. Updating List Values
"""
NumberList[3] = 100
for i in NumberList:
    print(i, ", ")  # Will be change value from 50 100'
print (len(NumberList))  # 4

"""
4. Updating List Values
"""
NumberList += [99]
for i in NumberList:
    print(i, ", ")  # Will add new index 99
print(len(NumberList))  # will be 5

"""
5. Adding Two Lists
"""
NumberList2 = [121, 30, 140, 150]

NumberList3 = NumberList + NumberList2
print(NumberList3)

"""
5. Comparing List
"""
NumberListForCompare = [121, 30, 140, 150]
print(NumberListForCompare == NumberList2)


# -------------------------------------- TUPLE --------------------------------

employeeTuple = ("Jas", "Sample", 22)
singleElementTuple = ("Sales", )  # comma in the last tells if it is tuple
print(employeeTuple[0])

employeeTuple1 = employeeTuple  # This is pointing to object same in the memory
print(id(employeeTuple1))  # Print the memory location should be same as next
print(id(employeeTuple))  # Print the memory location should be same as previous

"""
1. Adding contents to tuple will create a new tuple as tuples are immutable
"""

employeeTuple += (30, 20)

print(employeeTuple)   # ('Jas', 'Sample', 22, 30, 20)
print(employeeTuple1)  # ('Jas', 'Sample', 22)

# --------------------- MANIPULATING LIST AND TUPLE ---------------------

"""
2. Tuple Can be added to List i.e. List can be added with any iterable object
"""

NumberList += employeeTuple

print (NumberList)  # [20, 30, 40, 100, 99, 'Jas', 'Sample', 22, 30, 20]

"""
3. Tuple Can mutable objects and that can be modified like list in tuple is mutable
"""

newEmployeeTuple = ("John", [10, 20, 40])

newEmployeeTuple[1][2] = 50
print(newEmployeeTuple)  # ('John', [10, 20, 50]) Value of 2nd index is modified to 50


# Swaping Sequence
num1 = 1
num2 = 5

num1, num2 = (num2, num1)

# unpacking tuple or list
name, scores = newEmployeeTuple
print(name)  # John
print(scores)  # [10, 20, 50]

# Adding index number to tuple or list
employee = ["John", "Mary", "Tom"]
empListWithIndex = list(enumerate(employee))
empTupleWithIndex = tuple(enumerate(employee))
print(empListWithIndex)  # [(0, 'John'), (1, 'Mary'), (2, 'Tom')]
print(empTupleWithIndex)  # ((0, 'John'), (1, 'Mary'), (2, 'Tom'))

for index, name in empListWithIndex:
    print(f'{name}, {index}')

numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numberList[2:6])  # [2, 3, 4, 5]
print(numberList[:6])  # [0, 1, 2, 3, 4, 5]
print(numberList[6:])  # [6, 7, 8, 9, 10]
print(numberList[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numberList[::2])   # [0, 2, 4, 6, 8, 10] Skipping the number
print(numberList[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numberList[-1:-9:-1])  # [10, 9, 8, 7, 6, 5, 4, 3]
