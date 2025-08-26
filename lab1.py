#Problem 1

import math

#The area of a circle with radius 5.
radius = 5
area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is {area:f}.")

#The volume of a sphere with radius 3.
radius = 3
volume = 4/3 * math.pi * radius ** 3

print(f"The volume of the circle with radius {radius} is {volume:f}.")

#The hypotenuse of a right-angled triangle with sides 3 and 4.
a = 3
b = 4

hypotenuse = math.sqrt(a**2 +b**2)

print(f"The hypotenuse of a right-angled triangle with sides {a} and {b} equal {hypotenuse:f}.")

#Problem 2

#A string variable.
name = "Aurora Price"

#Length of name.
length = len(name)
print(length, "letters is the length of my name.")

#Concatenate name with a space in between.
first_name = "Aurora"
last_name = "Price"
print(first_name, last_name)

#Convert name to uppercase and lowercase.
full_name = "Aurora Price"
print(full_name.upper())
print(full_name.lower())

#Problem 3

#Create variables to store your age, height (in feet), and weight (in pounds).
age = 20
height_in_feet = 5.7
height_in_inches = 67
weight = 125

#Print the data type of each variable.
print(type(age))
print(type(height_in_feet))
print(type(weight))

#Calculate Body Mass Index
BMI= weight / (height_in_inches ** 2) *703

#Print BMI.
print(BMI)