# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must be unique and you may
# return the result in any order.
def intersection(nums1,nums2):
    '''
    input: 2 Lists of integers    
    output: list[integers]
    '''
    intersections = set()
    for value in nums1:
        if value in nums2:
            intersections.add(value)
    return [value for value in intersections]

nums1=[1,2,2,1]
nums2=[2,2]
print(intersection(nums1,nums2))