my_list = [1, 2, 3]

my_list = ['string', 100, 23.2]

print(len(my_list))

mylist = ['one', 'two', 'three']

print(mylist[0])

print(mylist[1:])

another_list = ['four', 'five']

print(mylist + another_list)

new_list = mylist + another_list

print(new_list)

new_list[0] = new_list[0].upper()

print(new_list)


new_list.append('six')
new_list.append('seven')
print(new_list)

popped_item = new_list.pop()
print(popped_item)


new_list.pop(-1)
print(new_list)


new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 7, 1, 2, 8, 3]

new_list.sort()
num_list.sort()

print(new_list)
print(num_list)


new_list.reverse()
num_list.reverse()

print(new_list)
print(num_list)