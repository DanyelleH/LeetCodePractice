# def pivotIndex(nums):
#     '''
#     input: List[int]
#     output: int - first index where L side == right side of the array,
#         if none, return -1
#     pivot index: where the l side of the list & r side of the list is equal.
#         PSEUDOCODE
#         1. 
#     '''
#     pointer = 0
#     for i in range(len(nums)):
#         if sum(nums[:i]) == sum(nums[i+1:]):
#             return i
#     return -1
    
# nums =[1,7,3,6,5,6]
# print(pivotIndex(nums))


# def dominantIndex (nums):
#     '''
#     input: List [int]
#     output: Index of the number that is atleast 2* every other list element.
#     '''
#     largest_integer = max(nums)
#     for num in nums:
#         if num != largest_integer:
#             if num*2 <= largest_integer:
#                 continue
#             else:
#                 return -1
#     return (nums.index(largest_integer))

# print(dominantIndex([3,6,1,0]))


# def plusOne(digits):
#     '''
#     Input: Array of integers, representing a large integer ( ex. [1,2,3] is 123 )
#     Output: array of digits

#     PSEUDOCODE
#         1. Increment the last number in the input array
#         2. return the new list. 
    
#     '''
#     #1. Increment the last digit
#     digits[-1] +=1
#     # 2. Starting from the end of the list, check if values are > 9.
#     for i in range(len(digits) -1,-1,-1): # going from right to left because thats how stacked expressions are solved in math.
#         if digits[i] >9:
#             digits[i] = 0

#             if i == 0:
#                 digits.insert(0,1)
#             else:
#                 digits[i-1] +=1
#         else:
#             break
#     return digits

    # for num in digits:
    #     if num < 9:
    #         new_digits= [int(digit) for digit in str(num)]
    #         digits.pop(-1)
    #         digits.extend(new_digits)
    # return digits
# print(plusOne([9,9]))




def rotate_letter(s,goal):
        if s == goal:
            return True

        else:
            print(s)
            return rotate_letter(s[1:] + s[0], goal) if s[1:] + s[0] != s else False
        
s='abcde'
goal="cdeab"
print(rotate_letter(s,goal))