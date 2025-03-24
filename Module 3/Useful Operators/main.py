for num in range(0, 10, 2):
    print(num)

print('\n')

word = 'abcde'

for index, letter in enumerate(word):
    print(index, letter)

print('\n')

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']

for item in zip(mylist1, mylist2):
    print(item)

print('\n')

d = {'mykey': 'myvalue'}

print(2 in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('x' in [1, 2, 3])
print('mykey' in {'mykey': 'myvalue'})
print('myvalue' in d.values())

print('\n')

mylist = [10, 20, 30, 40, 100]

print(min(mylist))
print(max(mylist))

print('\n')

from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(mylist)

print(mylist)

print('\n')

from random import randint

print(randint(0, 100))

print('\n')

result = int(input('What is your favorite number?\n'))

print(result)
