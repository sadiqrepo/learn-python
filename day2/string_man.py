#Subscripting
print("Hello"[4])

#string
print("123" + "345")

#Integer = whole number
print(123 + 345)

# For large integers, comma can be substituted with underscore
print(1_25_000)

# Decimal = Floating point number
print(3.14159)

#Boolean
print(True)
print(False)

# Type error
#len(123) -> can accept only string and not integer

# check data type
print(type("Hello"))
print(type(123))
print(type(True))
print(type(3.14159))

# Type casting / Data conversion

print(int("123") + int("456"))

int()
float()
str()
bool()

#print("Number of letters in your name: " + str(len(input("Enter you name\n"))))

name_of_the_user = input("Enter you name\n")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))
print(type(length_of_name))

print("Number of letters in your name: " + str(length_of_name))


