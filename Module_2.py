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
print(f"Age as a float:, {age:.2f}")
#"float" is applied to months old because we put 11 in "" so it is currently a string which is text to python. Normally you would put 11 in "" but we did
# this to show you how to convert a string to a float which is a number with decimals and even exponents. Applying float to years old is redundant because
# 25 is already an integer so it is compatible with float already

age = int(age)
print("Age as an int:", age)