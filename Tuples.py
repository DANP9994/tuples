number= 2*3*6
print(number)



def last(n):
    return n[-1]

# Define a function called 'sort_list_last' that takes a list of tuples 'tuples' as input
def sort_list_last(tuples):
    # Sort the list of tuples 'tuples' using the 'last' function as the key for sorting
    return sorted(tuples, key=last)

# Call the 'sort_list_last' function with a list of tuples as input and print the sorted result
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


from collections import Counter

# Create two dictionaries 'd1' and 'd2' with key-value pairs.
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Use the 'Counter' class to create counter objects for 'd1' and 'd2', which count the occurrences of each key.
# Then, add the counters together to merge the key-value pairs and their counts.
d = Counter(d1) + Counter(d2)

# Print the resulting merged dictionary 'd'.
print(d)



n = int(input("Input a number "))

# Create an empty dictionary 'd' to store the square of numbers.
d = dict()

# Iterate through numbers from 1 to 'n' (inclusive).
for x in range(1, n + 1):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x * x

# Print the dictionary 'd' containing the squares of numbers from 1 to 'n'.
print(d) 


price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Sort the 'price' list based on the price values (the second element in each tuple).
# The 'key' argument specifies a lambda function to convert the price strings to float values.
# Sorting is done in reverse (descending) order using the 'reverse' argument.
sorted_price = sorted(price, key=lambda x: float(x[1]), reverse=True)

# Print the 'sorted_price' list, which contains the items sorted by price in descending order.
print(sorted_price)


print("Create a new set:")

# Initialize an empty set and assign it to the variable 'x':
x = set()

# Print the empty set 'x':
print(x)

# Print the data type of 'x', which should be 'set':
print(type(x))

# Print a newline for separation:
print("\nCreate a non-empty set:")

# Create a non-empty set 'n' with the elements 0, 1, 2, 3, and 4 using a set literal:
n = set([0, 1, 2, 3, 4])

# Print the non-empty set 'n':
print(n)

# Print the data type of 'n', which should be 'set':
print(type(n))

# Print a newline for separation:
print("\nUsing a literal:")

# Create a set 'a' using a set literal with elements 1, 2, 3, 'foo', and 'bar':
a = {1, 2, 3, 'foo', 'bar'}

# Print the data type of 'a', which should be 'set':
print(type(a))

# Print the set 'a':
print(a) 



num_set = set([0, 1, 2, 3, 4, 5])

# Iterate through the elements in 'num_set' and print them with a space separator:
for n in num_set:
    print(n, end=' ')

# Print two newline characters for separation:
print("\n\nCreating a set using string:")

# Create a set 'char_set' using a string, which will create a set of unique characters from the string "w3resource":
char_set = set("w3resource")

# Iterate through the elements in 'char_set' and print them with a space separator:
for val in char_set:
    print(val, end=' ') 


    color_set = set()

# Print the empty set 'color_set':
print(color_set)

# Print a newline for separation:
print("\nAdd single element:")

# Add a single element "Red" to the 'color_set':
color_set.add("Red")

# Print the 'color_set' with the added element "Red":
print(color_set)

# Print a newline for separation:
print("\nAdd multiple items:")

# Add multiple elements "Blue" and "Green" to the 'color_set' using the 'update' method:
color_set.update(["Blue", "Green"])

# Print the 'color_set' with the added elements "Blue" and "Green":
print(color_set) 