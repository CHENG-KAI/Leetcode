def summaryRanges(nums):
    temp = []
    res = []
    begin = 0
    for i in xrange(len(nums)):
        if i == 0 or nums[i]!= nums[i-1]+1:
            res.append(str(nums[i]))
        elif i == len(nums) and nums[i]!=nums[i-1]+1:
            res.append(str(nums[i]))
        elif i == len(nums) and nums[i] == nums[i-1]+1:
            res[len(res)-1] += '->' + str(nums[i])
        elif nums[i] != nums[i+1] - 1:
            res[len(res)-1] += '->' + str(nums[i])
    return res
            
            
            
    
#easy understand by using head 
def summaryRanges(nums):
    if not nums:
        return []
    
    nums = nums + [nums[-1]+3]
    res = []
    head = nums[0]
    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] > 1:
            if head == nums[i-1]:
                res.append(str(head))
            else:
                res.append(str(head) + "->" + str(nums[i-1]))
            head = nums[i]
    return res
            

nums = [0,1,2,4,5,7]
summaryRanges(nums)
