    # Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
def minSubArrayLen( target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    current_sum = 0
    subarray_length = float('inf')
    left = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        # add the value of the rightmost element of nums to the current sum.
        while current_sum >= target:
             # while the current sum is too large, decrement sum by the value at the key [left] 
            subarray_length = min(subarray_length, right-left +1) 
            # difference between pointers, with index inclusivity compensation.
            current_sum -= nums[left]
            left +=1
    return subarray_length if subarray_length != float('inf') else 0
    



# target = 7
# nums = [2,3,1,2,4,3]

# target = 4
# nums = [1,4,4]

# target = 11
# nums = [1,1,1,1,1,1,1,1]
target=11
nums=[1,2,3,4,5]
print(minSubArrayLen(target, nums))