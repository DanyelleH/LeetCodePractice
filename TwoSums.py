# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
    nums = sorted(nums)
    left=0
    right=len(nums)-1
    while left < right:
        if nums[left] + nums[right] >target:
            right -=1
        if nums[left] + nums[right] < target:
            left +=1
        if nums[left] + nums[right] == target:
            return left , right

nums= [2,7,11,15]
target = 9
print(twoSum(nums,target))