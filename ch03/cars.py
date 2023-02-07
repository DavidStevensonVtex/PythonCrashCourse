# Organizing a List

# Sorting a List Permanently wit the sort() Method

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
cars.sort()
print(f"sorted cars: {cars}")

cars.sort(reverse=True)
print(f"reverse sorted cars: {cars}")

# Sorting a List Temporarily with the sorted() Function

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

# Printing a List in Reverse Order

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
print("\nHere is the original list:")
print(cars)

cars.reverse()
print("\nHere is the reversed list:")
print(cars)

# You can revert to the original order anytime by applying reverse() to the same list a second time.

# Finding the Length of a List

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
print(f"\nNumber of cars: {len(cars)}.")

# Avoiding Index Errors When Working With Lists

# motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
# print(motorcycles[3])
# Traceback (most recent call last):
#   File "D:\drs\Python\PythonCrashCourse\ch03\cars.py", line 44, in <module>
#     print(motorcycles[3])
# IndexError: list index out of range

# Keep in mind that whenever you want to access the last item in a list  you use the index -1.
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(f"\nLast motorcycle: {motorcycles[-1]}")

# The only time this approach will cause an error is when you request the last item from an empty list.

motorcycles = []
print(motorcycles[-1])
# Traceback (most recent call last):
#   File "D:\drs\Python\PythonCrashCourse\ch03\cars.py", line 57, in <module>
#     print(motorcycles[-1])
# IndexError: list index out of range