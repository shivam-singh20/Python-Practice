num = int(input("Enter a number: "))

for i in range(2,num):
    if num % i == 0:
        print("Number is not prime!")
        exit()

print("Number is prime!") 