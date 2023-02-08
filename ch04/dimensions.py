# Tuples

# However, sometimes you'll want to create a list of items that cannot change.
# Tuples allow you to do just that. Python refers to values that cannot 
# change as immutable, and an immutable list is called a tuple.

# Defining a Tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
# Traceback (most recent call last):
#   File "D:\drs\Python\PythonCrashCourse\ch04\dimensions.py", line 13, in <module>
#     dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

# Tuples are technically defined by the presence of a comma; the parentheses make them
# look neater and more readable. If you want to define a tuple with one element, you
# need to include a trailing comma:

my_t = (3,)
print(my_t)

# Looping Through All Values in a Tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
# Original dimensions:
# 200
# 50

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
# Modified dimensions:
# 400
# 100

# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed through-
# out the life of a program.