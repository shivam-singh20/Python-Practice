items = ["apple", "banana", "orange", "apple", "mango"]

for i in items:
    if items.count(i) > 1:
        print(i)
        exit()
print('All items are unique')