def checkMode( nums):   
    majority_check = len(nums)/2
    counts ={}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] +=1
    for k,v in counts.items():
        if v > majority_check:
            return k
        
        
nums= [3,2,3]
print(checkMode(nums))