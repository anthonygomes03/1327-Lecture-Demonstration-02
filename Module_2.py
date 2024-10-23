"""
Description: Module 2 Demonstration
Author: Anthony Gomes
Date: October 22, 2024
Usage: To demonstrate content from Module 2
"""

#This is a single comment

absolute_value=abs(-12)
print('absolute value', absolute_value)

# Function embedded within another function
print('absolute value', abs(-12))

print("Hello World!")

print("I am", 25, "years old.")

print("apples", "oranges", "bananas" , sep=",")

name = "Anthony"
age = 22
print(f"My name is {name} and I am {age} years old.")
# "f" at the front allows you to use the curly brackets. If you take the f away it will print the variable place holders instead of the variables themselves

value = 3.14159
print(f"the value is {value:.2f}")
#.2f takes a number and rounds it to two decimal points. you have to add : after your variable if you want to add pieces to it. {value:.2f} GOOD. {value.2f} BAD
# Also changing the number in ".2f" to ".4f" would have it round to 4 decimal points instead of 2.

number = 12345
print(f"The number is {number:05}")
#it's very important that you add a 0 in front of whatever number you want to set it to. This trick doesn't seem to work with numbers with decimals

name = "Anthony"
print(f"Hello, {name:>10}.")
# :>10 puts ten spaces between the comma and the name

name = "Anthony"
age = 22
salary = 67293.21
is_employed = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_employed))
# This checks to see what type of variable it is 

age = 25
current_salary = 67293.21

age_and_salary = age + current_salary

months_old = "11"
years_old = 25

age = (float(years_old)) + (float(months_old) / 12)
print("Age as a float:", age)
#"float" is applied to months old because we put 11 in "" so it is currently a string which is text to python. Normally you would put 11 in "" but we did
# this to show you how to convert a string to a float which is a number with decimals and even exponents. Applying float to years old is redundant because
# 25 is already an integer so it is compatible with float already

age = int(age)
print("Age as an int:", age)

print("Age:", age)
age += 3
# adding the += both adds the value and also updates the variables count for any other times below that line the age variable is called

print("Age:", age)

# A list of mixed data values:
employee_data = ["A123", 55024.23, 595, True]

# A list of lists:
list_of_lists = [["A", "B", "C"], [1, "X", True], [False, 12, 5.5]]

# A list of integers:
daily_step_count = [10343, 9385, 7029, 10931, 5921, 5921]
# List indexes start at 0 not 1. so the [2] is actually 7029 which is the third one on the list normally, but the second one in python starting from 0
print(daily_step_count[2])

daily_step_count[4] = 100
print(daily_step_count)

# Appends the value 8694 to the end of the list.
daily_step_count.append(8694)
print(daily_step_count)

# Inserts the value 4473 before the current element 3.
daily_step_count.insert(3, 4473)
print(daily_step_count)

# Removes the first occurrence of the value 7029 from the list.
daily_step_count.remove(7029)
print(daily_step_count)

# Removes the last item from the list and captures it into the popped variable.
popped = daily_step_count.pop()
print(daily_step_count)
print(popped)

# Sets index_value to the index of the first occurrence of 5921.
index = daily_step_count.index(5921)
print(index)

# Sets count to the number of occurrences of 5921
count = daily_step_count.count(5921)
print(count)

# Sorts the elements of the list in ascending order.
daily_step_count.sort()
print(daily_step_count)

# Sort the elements of the list in descending order.
daily_step_count.sort(reverse=True)
print(daily_step_count)

# Sort the elements of the list in descending order.
daily_step_count.reverse()
print(daily_step_count)

red_river = ['R', 'R', 'C', ' ', 'P', 'o', 'l', 'y', 't', 'e', 'c', 'h', 'n', 'i', 'c']
print(red_river[2: 12: 2]) # from 2 to 12, stepping by 2

print(red_river[: 10: 1]) # from start (0) to 10, stepping by 1

print(red_river[5: : 3]) # from 5 to end(14), stepping by 3

print(red_river[::5]) # from start(0) to end(14), stepping by 5

print(red_river[-1: -5: -1]) # from last(14) to 5th last, stepping backwards by 1

provinces_and_territories = ('BC', 'AB', 'MB', 'SK', 'ON', 'QC', 'NB', 'NL', 'NS', 'PE', 'NT', 'NU', 'YT')

manitoba = provinces_and_territories[2]
print(manitoba)

random_tuple = (1, 66, 3, 7, 42, 78, 12, 55)

# The len() function return the number of elements in a tuple
length = len(random_tuple)
print(length)

# The max() function returns the element with the highest value in a tuple
max = max(random_tuple)
print(max)

# The min() function returns the element with the lowest value in a tuple
min = min(random_tuple)
print(min)

#The sum() function returns the sum of all elements in a tuple
sum = sum(random_tuple)
print(sum)

#The sorted() function returns a new list containing the elements of the original tuple in ascending order.
sorted_tuple = sorted(random_tuple)
print(sorted_tuple)

name = "John"
tuple_name = tuple(name)
print(tuple_name)

list_of_numbers = [1, 2, 3]
tuple_of_numbers = tuple(list_of_numbers)
print(tuple_of_numbers)

# Here are some examples of Dictionaries in action:
fruit_inventory = {'apples': 23, 'oranges': 10, 'bananas': 59, 'pears': 29}

value = fruit_inventory['oranges']
print(value)

fruit_inventory['oranges'] = 25
print(fruit_inventory['oranges'])

fruit_inventory['plums'] = 100
print(fruit_inventory)

# The keys() method returns a view list object of the keys in the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : "1964"
}

x = car.keys()
car["color"] = "white"
print(x)

# The values() method returns a view list object of the values in the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : "1964"
}

x = car.values()
car["year"] = 2018
print(x)

# The items() method returns a view list containing Tuples of the key-value pairs in the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : "1964"
}

x = car.items()
car["year"] = 2018
print(x)

# The get() method returns the value of the key arguement, or the specified default value.
fruit_inventory = {'apples': 23, 'oranges': 10, 'bananas': 59, 'pears': 29}

print (fruit_inventory.get('apples'))

print(fruit_inventory.get('plums', 'fruit is not currently in the dictionary'))

#The pop() method returns the value of the key argument and removes it from the dictionary
fruit_inventory = {
    'apples': 23, 
    'oranges': 10, 
    'bananas': 59, 
    'pears': 29
}

fruit_inventory.pop('oranges')

print(fruit_inventory)

#The clear() method removes all key-value pairs from the dictionary.
fruit_inventory = {
    'apples': 23, 
    'oranges': 10, 
    'bananas': 59, 
    'pears': 29
}

fruit_inventory.clear()

print(fruit_inventory)

# Two sets are created here, primes containing the values shown, and fives, an empty set.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
fives = set()

#The add() method adds an element to the set.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
fives = set()

primes.add(29)
fives.add(5)

print(primes)

print(fives)

#The remove() method removes an element from the set. If the element does not exist, an exception will occur.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}

primes.remove(3)

print(primes)

#The discard() method removes an element from the set. If the element does not exist, the statement is ignored.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}

primes.discard(3)

print(primes)

# no exception occurs
primes.discard(22)

#The union() method returns a new set containing all unique elements in the set object as well as the argument.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
fives = {5, 10, 15, 20, 25, 30, 35}

union = primes.union(fives)

print(union)

#The difference() method returns a new set containing all elements in the set object that are different from those elements in the argument.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
fives = {5, 10, 15, 20, 25, 30, 35}

difference = primes.difference(fives)

print(difference)

difference = fives.difference(primes)

print(difference)

#The intersection() method returns a new set containing all elements common to both the set object and the argument.
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
fives = {5, 10, 15, 20, 25, 30, 35}

intersect = primes.intersection(fives)

print(intersect)

# List, Tuple, and Strings are ordered collections. String and Tuple types can be converted to a list by using the list() function.
# Similarly, the tuple() function can be used to convert String and List types to a Tuple.

# String
message = "Hello World"

# Tuple
inventory_counts = (1, 5, 6, 43, 511)

# List
temperatures = [23, 27, 31, 20, 19]

# Cast string to a list
characters = list(message)

# Cast tuple to a list
inventory_counts = list(inventory_counts)

# Cast a string to a tuple
characters = tuple(message)

# Cast a list to a tuple
temperatures = tuple(temperatures)

# Iterable types can also be converted to a set.
# Because a set is a collection of unique elements, when casting to a set duplicate values will be omitted.
temperatures = [21, 22, 22, 23, 24, 24]

temperatures = set(temperatures)

print(temperatures)

message = "hello"

message = set(message)

print(message)