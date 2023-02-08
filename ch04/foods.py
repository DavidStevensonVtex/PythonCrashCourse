# Copying a List

my_foods = [ 'pizza', 'falafel', 'carrot cake' ]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
# ['pizza', 'falafel', 'carrot cake']

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ['pizza', 'falafel', 'carrot cake']

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ['pizza', 'falafel', 'carrot cake', 'ice cream']

# If we had simply set friend_foods equal to my_foods, we
# would not produce two separate lists.

# This doesn't work.

friend_foods = my_foods

print("\nMy favorite foods are:")
print(my_foods)
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ['pizza', 'falafel', 'carrot cake', 'cannoli']