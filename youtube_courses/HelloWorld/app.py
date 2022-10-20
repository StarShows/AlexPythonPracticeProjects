# Number
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