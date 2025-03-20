myfile = open('/home/felipe/workspace/others/grandchild/python-bootcamp/I-O with Basic Files in Python/myfile.txt')

content = myfile.read()

print(content)

content = myfile.read()

print("second read of the file\n\n", content) # returns nothing


myfile.seek(0)
content = myfile.read()

print(content)

myfile.seek(0)

print(myfile.readlines())

myfile.close()

with open('/home/felipe/workspace/others/grandchild/python-bootcamp/I-O with Basic Files in Python/myfile.txt') as my_new_file:
    content = my_new_file.read()


    print("\n\n\nusign with\n", content)


# mode = 'r' -> Read /\  mode = 'w' -> Write /\ mode = 'a' -> Append

# mode = 'r+' -> Reading and Writing
# mode = 'w+' -> Writing and Reading
with open('/home/felipe/workspace/others/grandchild/python-bootcamp/I-O with Basic Files in Python/myfile.txt', mode = 'r') as myfile:
    content = myfile.read()


    print(content)