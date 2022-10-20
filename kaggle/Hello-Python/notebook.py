from pydoc import describe


spam_amount = 0
print(spam_amount)

# ordering spam, eggs, Spam, baconand spam (4 more servings of spam)

spam_amount = spam_amount + 4

if spam_amount> 0:
    print("But I don't want ANY spam!")
    
viking_song = "Spam" * spam_amount
print(viking_song)


spam_amount = 0

print(type(19.95))

a = 11
b = 12

print(a ** -b)
print(-3 +4  *2)

hat_height_cm = 25
my_height_cm = 190

# How tall am I in meters when wearign my hat
total_height_meters = (hat_height_cm + my_height_cm ) / 100

print(" Height in meters = ", total_height_meters, "?")


print(min(2,2,3,1))
print(max(2,32,7))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.8))

number = 19.95
print(number * 6)

# Describe the type of variable
def check_type(value):
    output = type(value)
    return output

check_type = check_type(number)
print(check_type)


# Prototype methods:
# Outputs info to the log
print('Hello Alex')
# Preform a type check
type('this is a string') # - string
