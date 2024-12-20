def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    look at the nums list, if theres more than 2 of the number, remove any 
    additional of the same number
    """
    seen={}
    current_index= 0

    for num in nums:
        if num not in seen:
            seen[num] = 1
            nums[current_index] = num
            current_index +=1
        elif seen[num] <2:
            seen[num] +=1
            nums[current_index] = num
            current_index +=1
    del nums[current_index:] # removes value on end of list
    return nums

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))