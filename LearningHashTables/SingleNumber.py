
# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use 
# only constant extra space.

def SingleNum(nums):
    # input: list
    # output: integer
    nums.sort()
    i=0
    while i<len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
            nums.pop(i)
        else:
            return nums[i]
    return nums[i]
    #check if there are 2+ of each value in the array. if not, return that value.

nums=[4,1,2,1,2]
nums2=[2,2,1]
print(SingleNum(nums))
print(SingleNum(nums2))