# Functions in Python

### Greet User Function

'''python'''
def greet_user(name, greeting="Hello"):
    print(f"{greeting} {name}!")

# # Test the function
greet_user("John")
greet_user("Jane", "Hi")

def sum_numbers(a, b):
    return a + b

# # Test the function
result = sum_numbers(2, 3)
print(result)

fruits = ["apple", "banana", "cherry", "date"]

# # Iterate over the list
fruits.append("elderberry")
print(fruits)

# # remove banana 
fruits.remove('banana')
print(fruits)

# # insert "blueberry" at index 1
fruits.insert(1, 'blueberry')
print(fruits)

# # sort the list in aphabetical order
fruits.sort()
print(fruits)


# write a loop that prints the numbers from 1 to 10

for i in range (1, 11):
    if i == 7:
        break
    print(i)

# Loop with continue statement
for i in range (1, 11):
    if i % 3 == 0:
        continue
    print(i)

