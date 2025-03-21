mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print(num)

for num in mylist:
    print('Hello')

for num in mylist:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
print(list_sum)


for letter in 'Hello World':
    print(letter)

print('\n\n')

tup = (1, 2, 3)

for item in tup:
    print(item)

print('\n\n')

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]

for a, b in mylist:
    print(a)
    print(b)

print('\n\n')

mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]

for a, b, c in mylist:
    print(b)

print('\n\n')

d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(value)