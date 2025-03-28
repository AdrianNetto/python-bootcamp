# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a, b):
    result = a + b
    if result == 20 or a == 20 or b ==20:
        return True
    else:
        return False
    
print(makes_twenty(12, 8))
print(makes_twenty(20, 1))
print(makes_twenty(2, 7))