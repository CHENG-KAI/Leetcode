def combinationSum(nums,target):
    res = []
    dfs(nums,target,0,[],res)
    return res
    

def dfs(nums,target,index,path,res):
    
    if target == 0:
        res.append(path)
        return    
    for i in xrange(index,len(nums)):
        if nums[i] > target:
            break
        dfs(nums,target-nums[i],i,path+[nums[i]],res)
nums = [2,3,5,7]
target = 7
print combinationSum(nums, target)
