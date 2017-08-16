def subsets(nums):
    res = []
    
    dfs(nums,0,[],res,len(nums))
    return res
def dfs(nums,index,path,res,l):
    
    #if len(path) <= len(nums):
    res.append(path)
        #return
    
    for i in xrange(index,len(nums)):
        dfs(nums,i+1,path+[nums[i]],res,l)
    
        
        
        
    
    

nums = range(1,5)
print subsets(nums)
