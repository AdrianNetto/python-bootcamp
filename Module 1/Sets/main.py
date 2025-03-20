myset = set()

print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset)

myset.add(2) # will not add, because the number two are already in the set. Needs to be unique
print(myset)

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

print(set(mylist))
