def combinationSum(nums,target):
    res = []
    nums.sort()
    dfs(nums,target,0,[],res)
    finalres = []
    for i in res:
        if i not in finalres:
            finalres.append(i)
        else:continue
    return finalres
            
        

def dfs(nums,target,index,path,res):
    
    if target == 0:
        res.append(path)
        return    
    for i in xrange(index,len(nums)):
        if nums[i] > target:
            break
        dfs(nums,target-nums[i],i+1,path+[nums[i]],res)
    
        
    
    
nums = [10, 1, 2, 7, 6, 1, 5]
target = 8
print combinationSum(nums, target)
