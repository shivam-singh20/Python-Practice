type_animal = str(input("Enter your pet type: "))

animal_age = int(input("Enter your pet age: "))

if type_animal == "dog" and animal_age <= 2:
    print("Puppy Food")
elif type_animal == "dog" and animal_age > 2:
    print("Dog Food")
elif type_animal == "cat" and animal_age >= 5:
    print("Senior cat food")
elif type_animal == "cat" and animal_age < 5:
    print("Kitten food")
else:
    print("animal not determined")