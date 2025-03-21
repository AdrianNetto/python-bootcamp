x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1

x = [1, 2, 3]

for item in x:
    pass

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

for letter in mystring:
    if letter == 'a':
        break
    print(letter)
