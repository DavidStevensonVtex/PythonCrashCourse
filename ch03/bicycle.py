bicycles = [ 'trek', 'cannondale', 'redline', 'specialized' ]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# Index positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])

# Print the last element in the list
print(bicycles[-1])

# Using individual values from a list

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)