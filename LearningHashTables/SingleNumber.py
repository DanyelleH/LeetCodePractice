from collections import Counter
# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use 
# only constant extra space.

def SingleNum(nums):
    # input: list
    # output: integer
    counts = Counter(nums)
    for num, count in counts.items():
        if count ==1:
            return num
        
nums=[4,1,2,1,2]
nums2=[2,2,1]
print(SingleNum(nums))
print(SingleNum(nums2))