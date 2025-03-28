x= 25

def printer():
    x = 50
    return x

print(x)
print(printer())


name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy'

    def hello():
        name = 'Local'
        print('Hello', name)
    
    hello()

greet()

x = 50

def func():
    global x
    print(f'X is equal to {x}')

    x = 200
    print(f'I just locally changed global X, and now is {x}')

func()
print(x)