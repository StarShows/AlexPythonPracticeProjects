# Youtube video learning notes from video:
# https://www.youtube.com/watch?v=kqtD5dpn9C8
# Programing with mosh
# Alexander Tannenbaum pyhton course notes


# Number
import types


age = 20
age = 30

price = 19.95
# String
first_name = "Alex"

# Boolean
is_online = True



# Print
print(age)

# Exercise
# - We check in a patient named john smith
# - He is 20 years old
# - He is a new patient

# Input from user
name = input("What is your name? ")
if name:
    print("Hello " + name + "!")

    #  Value conversions
    birth_year = input("Enter your birth year: ")
    birth_year = int(birth_year)
    age = 2022 - birth_year
    print("oh cool, so you are " + str(age) + " years old?")

    confirm_age = input("Yes/No ")
    if confirm_age == "Yes":
        print("awesome!")
    else:
        print("oh damn")
        
    
# Float convert type
print(float(10))

# Bool convert type
print(bool(1))

# String convert type
str(12)

# Exercise 2
first_number = float(input("First: "))
second_number = float(input("Second: "))
sum = first_number + second_number
print("Sum: ", first_number+second_number)

# def checkInPatient(name, age, isNew):
    # print("Patient" name " is " age " years old")


# Lesson 3 - strings
course = "Python for Beginners"
# Find the index where a string matches the origin
print(course.find('Python'))

#  Replace characters in a string
print(course.replace('for', '4'))

# Find 'in' operator
print('Python' in course )
# Make string upper case
print(course.upper())

print(course)


# Lesson 4 - arithmetic operations
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x+3
x+=3
print(x)
x = x-3
x-=3
print(x)

x = 10+3*2
print(x)
x = (10+3)*2
print(x)

# Lesson 5 - Comparison Operators
# >
# <
# <=
# >=
# !=
x = 3 != 2  
print(x)

# Lesson 6 - logical operators
price = 25
# and is the alternate to &&
print(price > 10 and price < 30)

price = 5

# or opertaor is simular to js || operator
print(price > 10 or price < 30)

# Not operator (!)
price = 25
print(not price > 10)
# and (both)
# or (atleast one)
# not (inverts value)

# Lesson 7 - if statements
temperature = 27

if temperature > 30:
    print("It's a hot day today")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30)
    print("It's a nice day")
elif temperature> 10: #(10, 20]
    print("It's a bit cold")
else:
    print("It's cold")

print("done")

# Exercise
# Weight converter program
weight = input("Weight:")
mesure_unit = input("(K)g or (L)bs")
if mesure_unit.upper() == "K":
    print("weight in Lbs is ", float(weight)*0.45359237)
elif mesure_unit.upper() == "L":
    print("Your weight in Kg is ",float(weight)/2.2 )
else:
    print("Plase enter a valid wight")
    
    
# Lesson 8 - while loops
print("1")
print("2")
print("3")
print("4")
print("5")

# While loops
i = 1;
while i <= 10:
    print(i* '*')
    i = i + 1
    
# Lesson 9 - lists
1
1.1
True
'a'
# - basic types
# complex types:
names = ["John", "bob", "alex","zev","evan"]
print(names[-1]) # represents last item on list

# complex types:
names = ["John", "bob", "alex","zev","evan"]
print(names[-2]) # represents second to last item on list
# Updated list item value by index
names[0] = "Jon"
print(names)


# Select range of values
names = ["John", "bob", "alex","zev","evan"]
print(names[0:3])
print(names)

# Lesson 10 - list methods
# String in python are objects, they have capabilities
"a".upper();
numbers = [1,2,3,4,5]
# Insert number at the end of a list
numbers.append(6)
print(numbers)

# Insert number at the middle or beginning
numbers = [1,2,3,4,5]
numbers.insert(4,-1)
print(numbers)

# Remove items 
numbers = [1,2,8,4,8,8]
numbers.remove(8)
print(numbers)

# Remove all items in a list
numbers = [1,2,8,4,8,8]
numbers.clear()
print(numbers)

# Check if an item exists in a list
numbers = [1,2,8,4,8,8]
print(10 in numbers)

# Check how many numbers are in a list
print(len(numbers))

# Lesson 11
# for loop
numbers = [1,2,8,4,8,8]

for item in numbers:
    print(item)

# While loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i+1

# Lesson 12 - the range() function
numbers = range(5,10)
print(numbers)
for number in numbers:
    print(number)

# add a step to the range
numbers = range(5,10,3)
print(numbers)
for number in numbers:
    print(number)

# shorthand
# numbers = range(5,10,3)
# print(numbers)
for number in range(5):
    print(number)

# Lesson 13 - Tuples
numbers = (1,2,3, 3)
numbers[0] = 3
numbers.count()
