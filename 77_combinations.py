def combine(n, k):
    res = []
    
    dfs(range(1,n+1),0,[],res,k)
    return res
def dfs(nums,index,path,res,k):
    if len(path) == k:
        res.append(path)
        return
    if len(path) + len(nums[index:])<k:return
    for i in xrange(index,len(nums)):
        dfs(nums,i+1,path+[nums[i]],res,k)
    
        
        
        
    
    

n = 10
k = 3
print combine(n,k)


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools 
        return [ x for x in itertools.combinations(range(1,n+1),k)]
