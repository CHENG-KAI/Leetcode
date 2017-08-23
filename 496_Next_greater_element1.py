def nextGreaterElement(findNums, nums):
      
    res = []
    for i in findNums:
        for j in nums[nums.index(i):]:
            if j > i:
                res.append(j)
                break
        
        else:
            res.append(-1)
        
                
    return res
findNums = [4,1,2]
nums = [1,3,4,2]
print nextGreaterElement(findNums, nums)
