from functions import square
import functions

# first import
for i in range(10):
    print(f"The square of {i} is {square(i)}")

# second import
for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
