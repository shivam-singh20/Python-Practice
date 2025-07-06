score = int(input("Enter marks of student: "))

if score>=100:
    print("Invalid Marks")
    exit()

if score>=90:
    print("A grade")
elif score>=80:
    print("B grade")
elif score>=70:
    print("C grade")
elif score>=60:
    print("E grade")
else:
    print("F grade")