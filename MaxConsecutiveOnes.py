# Given a binary array nums, return the maximum number of consecutive 
# 1's in the array if you can flip at most one 0.

def MaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    zeroes_changed = 0
    sequence_start = 0
    longest_so_far = 0
    current_length =0
    
    for sequence_end in range(len(nums)):
        if nums[sequence_end] == 1:
            current_length +=1
        elif nums[sequence_end] == 0:
            zeroes_changed += 1
            current_length +=1
            
        while zeroes_changed >1:
            if nums[sequence_start] == 0:
                zeroes_changed -=1
            sequence_start +=1
            current_length -=1
        
        longest_so_far = max(longest_so_far , current_length)
        
    return longest_so_far
            
                
nums= [1,0,1,1,1,1,1,0,0,0,0,0,1,0]
print(MaxConsecutiveOnes(nums))