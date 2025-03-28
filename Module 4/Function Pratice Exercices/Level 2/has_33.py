# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    string = ''

    for num in nums:
        string += str(num)
    
    if '33' in string:
        return True
    else:
        return False


print(has_33([1, 2, 3, 3]))
print(has_33([1, 2, 3, 4]))