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

# A list of mixed data values:
employee_data = ["A123", 55024.23, 595, True]

# A list of lists:
list_of_lists = [["A", "B", "C"], [1, "X", True], [False, 12, 5.5]]