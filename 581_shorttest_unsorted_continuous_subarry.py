def findUnsortedSubarray(nums):
    
    n = len(nums)
    a = sorted(nums)
    l , r = 0 , n-1
    res = []
    while l <= r:
        if nums[l] != a[l]:
            res.append(l)
        if nums[r] != a[r]:
            res.append(r)
        
        l+=1
        r-=1
    if not res:
        return 0
    return max(res) - min(res) + 1
