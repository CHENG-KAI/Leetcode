def findMedianSortedArrays(nums1, nums2):
    num = nums1 + nums2
    num.sort()
    n = len(num)/2
    if len(num) & 1 == 1:
        return num[n]
    else:
        return float(num[n-1] + num[n])/2
        
    
    
    
    
nums1 = [1,3]
nums2 = [2]
findMedianSortedArrays(nums1, nums2)
