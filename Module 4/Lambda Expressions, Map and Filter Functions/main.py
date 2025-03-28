def square(num):
    return num ** 2

mynums = [1, 2, 3, 4, 5, 6]

for item in map(square, mynums):
    print(item)

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0

print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)

def square1(num):
    result = num ** 2
    return result

print(square1(3))

square2 = lambda num: num ** 2

print(square2(5))

print(list(map(lambda num: num ** 2, mynums)))

print(list(filter(lambda num: num % 2 == 0, mynums)))

print(list(map(lambda name:name[::-1], names)))