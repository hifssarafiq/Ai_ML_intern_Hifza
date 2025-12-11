# 1. LIST OPERATIONS
print("LIST OPERATIONS")
# Create a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Add an item
fruits.append("orange")
print("After append:", fruits)

# Remove an item
fruits.remove("banana")
print("After remove:", fruits)

# Access an item
print("First item:", fruits[0])

# Loop through list
print("Loop through list:")
for fruit in fruits:
    print(fruit)
print("\n")
# 2. TUPLE OPERATIONS
print("TUPLE OPERATIONS ")
# Create a tuple
numbers = (1, 2, 3, 4, 5)
print("Original tuple:", numbers)

# Access an item
print("Third item:", numbers[2])

# Tuples are immutable, so you cannot add or remove items
new_numbers = numbers + (6, 7)
print("After concatenation:", new_numbers)

print("\n")
# 3. DICTIONARY OPERATIONS
print(" DICTIONARS ")
# Create a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Original dictionary:", person)

# Access a value
print("Name:", person["name"])

# Add a key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Remove a key-value pair
person.pop("age")
print("After removing age:", person)

# Loop through dictionary
print("Loop through dictionary:")
for key, value in person.items():
    print(key, ":", value)

print("\n")
# 4. SET OPERATIONS
print("SET OPERATIONS ")
# Create a set
colors = {"red", "green", "blue"}
print("Original set:", colors)

# Add an item
colors.add("yellow")
print("After add:", colors)

# Remove an item
colors.remove("green")
print("After remove:", colors)

# Check membership
print("Is 'red' in colors?", "red" in colors)

# Set operations: union, intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)          # or set1.union(set2)
print("Intersection:", set1 & set2)   # or set1.intersection(set2)
