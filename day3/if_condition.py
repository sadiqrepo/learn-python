print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
print(f"Your current height is: {height} cms.")
allowed_height = 120
if height >= allowed_height:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everthing is going to be ok. Have a free ride on us!")
    else: 
        bill = 12
        print("Adults tickets are $12.")
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print(f"Sorry, you have to grow over or equal to {allowed_height} cms before you can ride!")
    

# Modulo operator
number_to_check = int(input("What is the number you want to check? "))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
# Nested if statements

