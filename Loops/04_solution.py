string = str(input("Enter your string: "))
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(string,"is reversed to",reversed_string) 