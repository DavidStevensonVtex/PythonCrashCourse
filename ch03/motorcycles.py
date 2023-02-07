# Modifying elements in a list

motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list

# Appending elements to the end of a list
print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

print()
motorcycles = [] 
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting elements into a list

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an Item using the del Statement

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
del motorcycles[0]
print(motorcycles)

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
del motorcycles[1]
print(motorcycles)

# Removing an Item using the pop() method

# Popping an item removes an item from the end of the list (top of the stack)

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"popped motorcycle: {popped_motorcycle}")

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# Popping Items from any Position in the list

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati' ]
print(motorcycles)

motorcycles.remove('ducati')
print(f"Removed ducati: {motorcycles}.")

print()
motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati' ]
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")