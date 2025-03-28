def say_hello():
    print('Hello')

say_hello()

def say_hello_name(name):
    print(f'Hello, {name}')

say_hello_name('Adrian')


def add_num(num1, num2):
    return num1 + num2

result = add_num(10, 20)

print(result)

def print_result(a, b):
    print(a + b)

def return_result(a, b):
    return a + b

print_result(50, 30) # cant assign to variables
return_result(50, 30)

def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(10, 20))
print(sum_numbers('10', '20'))
