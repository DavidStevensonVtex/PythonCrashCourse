squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(f"squares: {squares}\n")
# squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(f"squares: {squares}\n")
# squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
print(f"min(digits): {min(digits)}")
print(f"max(digits): {max(digits)}")
print(f"sum(digits): {sum(digits)}")

# List Comprehensions

squares = [value**2 for value in range(1,11)]
print(f"\nsquares: {squares}")