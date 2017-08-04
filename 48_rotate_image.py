def canJump(nums):
    reach = 0
    for i,e in enumerate(nums):
        if reach < i:
            return False
        reach = max(reach,i+e)
        
    return True
        
        
    
    
    

nums = [3,2,1,0,4]
canJump(nums)
