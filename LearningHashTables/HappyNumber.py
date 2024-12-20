'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares 
of its digits. 
Repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
def isHappy(num):
    '''
    input: integer
    output: bool
    '''
    # to prevent endless looping, we need to track values seen.
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) **2 for digit in str(num))

    return num == 1

print(isHappy(19))
print(isHappy(11))