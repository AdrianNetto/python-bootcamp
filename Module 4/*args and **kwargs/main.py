def myfunc(a, b, c=0, d=0):
    return sum((a, b, c, d)) * 0.05

print(myfunc(40, 60))


def function(*args):
    return sum((args)) * 0.05

print(function(1, 2, 3, 4, 5, 6, 7))


def anotherfunction(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

anotherfunction(fruit='apple')
anotherfunction()


def newfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

newfunc(10, 20, 30, food='BigTasty')