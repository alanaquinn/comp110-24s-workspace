"""Lesson 5 Conditionals"""

user_input: str = input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

#if user_number is less than 10, print "small"
#if user_number < 10:    
#   print("small")
#else:
#    print("large")

#print(user_number)

# this class is stupid. if user_number is even, print "even"
if user_number % 2 == 0:
    print("even")
else:
    print("odd")

print(user_number)
