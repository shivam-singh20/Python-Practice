n = int(input("Enter size of n: "))

sum_even = 0

for i in range(0,n*2):
    if i%2 == 0:
        sum_even += i

print("Sum of first",n,"even number is:",sum_even)
