age = int(input("Enter an age: "))

day = input("Enter a day: ")

price = 12 if age >= 18 else 8

if(day == "Wed"):
    price -= 2

print("Price of the ticket is $",price)