def even_check(number):
    return number % 2 == 0
    

print(even_check(20))
print(even_check(21))

def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers

odd_numbers = [1, 3, 5, 7 ,9]
even_numbers = [2, 4, 6, 8, 10]
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(check_even_list(odd_numbers))
print(check_even_list(even_numbers))
print(check_even_list(numbers_list))

