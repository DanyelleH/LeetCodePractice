# Given an integer array nums, return true if any value appears at least twice in 
# the array, and return false if every element is distinct. You must implement a 
# solution with a linear runtime complexity and use only constant extra space.
def containsDuplicate(nums):
    '''
    input: list
    output: bool
    '''
    hashed_nums = set(nums)
    if len(hashed_nums) < len(nums):
        return True
    else:
        return False
nums= [1,2,3,4]
nums2=[1,2,3,1]
print(containsDuplicate(nums))
print(containsDuplicate(nums2))


