# name = "Harry"

# print(name[0])
# print(name[1])

# names = ["harry", "Ron", "Peter"]
# print(names)
# print(names[0])
 

# #### DATA STRUCTURES #####

# List - sequence of mutable values
# Define a list of names
names = ["harry", "Ron", "Peter", "Jane", "Kay"]
print(names)

# Adding other values to the end of the list
names.append("Tom")
names.sort()
print(names)


# tuple - sequence of immutable values

# Set - collection of unique values
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)
print(s)

s.remove(2)
print(s)
print(f"The set has {len(s)} elements")


# dict - collection of key-value pairs

houses ={"Harry": "Potter", "Mary":"Jane"}

houses["Chris"]="Potter"

print(houses["Harry"])
print(houses["Chris"])

