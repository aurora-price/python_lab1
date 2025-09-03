#Problem 1
from math import remainder

name = "Aurora Price"
age = 20
height = 5.7
favorite_color = "Purple"

print(name)
print(age)
print(height)
print(favorite_color)

print(name,age,height,favorite_color)

print(f"Hello: My name is {name} and my favorite color is {favorite_color}! I am {age} years old and I am {height} inches tall.")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

import math
radius = 5
circle_area = round(math.pi * radius ** 2,1)
print(f"The area of the circle is {circle_area}")

#Problem 2

import math
age_sqrt = math.sqrt(age)
print(age_sqrt)

height_sin = math.sin(height)
height_cos = math.cos(height)
print(height_sin)
print(height_cos)

#Problem 3
sum = age+5
difference = height-4
product = age*height
quotient = height/2
remainder = age%3
squared = age**2
print(f"""
Sum: {sum}
Difference: {difference}
Product: {product}
Quotient: {quotient}
Remainder: {remainder}
Squared: {squared}
""")

#Problem 4
Fahrenheit = float(input("Enter Fahrenheit: "))
Celsius = round((Fahrenheit - 32) * 5/9,1)
degree = u"\N{DEGREE SIGN}"
print(f"{Celsius}{degree}C")




