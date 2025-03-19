file_path = '/home/felipe/workspace/others/grandchild/python-bootcamp/I-O with Basic Files in Python/my_new_file.txt'

with open(file_path, mode = 'r') as f:
    print(f.read())


with open(file_path, mode = 'a') as f:
    print(f.write('\nFOUR ON FOURTH'))

with open(file_path, mode = 'r') as f:
    print(f.read())

with open('I-O with Basic Files in Python/test.txt', mode = 'w') as f:
    f.write('I CREATED THIS FILE')

with open('I-O with Basic Files in Python/test.txt', mode = 'r') as f:
    print(f.read())
