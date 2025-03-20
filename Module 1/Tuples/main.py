t = (1, 2, 3)

mylist = [1, 2, 3]

print(type(t))
print(type(mylist))

t = ('one', 2)

print(t[0])
print(t[-1])

t = ('a', 'a', 'b')

print(t.count('a'))
print(t.index('a'))

print(t)
print(mylist)

mylist[0] = 'NEW'

print(mylist)

# t[0] = 'NEW' --> invalid: 'tuple' object does not support item assignment