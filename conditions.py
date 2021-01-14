# n = input("Number: ")
# the input function doesn't consider the type of 
# to make it a number you need to wrap the whole expression in an int function
n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")    
else:
    print("n is zeroe")

# Traceback (most recent call last):
#   File "c:/Users/kace1/python/conditions.py", line 3, in <module>
    # if n > 0:
# TypeError: '>' not supported between instances of 'str' and 'int'

# This produces an error