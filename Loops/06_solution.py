num = int(input("Enter a number: "))
temp_num = num
factorial = 1

while temp_num > 0:
    factorial *= temp_num
    temp_num -= 1

if num < 0:
    print("Invalid input")
elif num > 0:
    print("Factorial of",num,"is",factorial)
else:
    print("Factorial of",num,"is",1)