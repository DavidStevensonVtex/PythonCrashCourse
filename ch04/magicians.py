# Chapter 4 - Working with Lists

# Looping through an Entire List

magicians = [ 'alice', 'david', 'carolina' ]
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop

print("\n")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing something After a for Loop

print("Thank you, everyone. That was a great magic show!")

# Avoiding Indentation Errors

# for magician in magicians:
# print(magician)
#   File "D:\drs\Python\PythonCrashCourse\ch04\magicians.py", line 23
#     print(magician)
#     ^
# IndentationError: expected an indented block

# Forgetting to indent additional lines

print("\n")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# Indenting Unnecessarily

# message = "Hello Python world!"
#     print(message)
#   File "D:\drs\Python\PythonCrashCourse\ch04\magicians.py", line 44
#     print(message)
# IndentationError: unexpected indent

# Indenting Unnecessarily After the Loop

# If you accidentally indent code that should run after a loop has finished, that
# code will be repeated once for each item in the list.

print("\n")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.

# Thank you, everyone. That was a great magic show!
# David, that was a great trick!
# I can't wait to see your next trick, David.

# Thank you, everyone. That was a great magic show!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# Thank you, everyone. That was a great magic show!


# Forgetting the Colon

# magicians = [ 'alice', 'david', 'carolina' ]
# for magician in magicians
#     print(magician)
#   File "D:\drs\Python\PythonCrashCourse\ch04\magicians.py", line 78
#     for magician in magicians
#                              ^
# SyntaxError: invalid syntax

