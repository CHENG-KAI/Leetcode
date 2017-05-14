def maxproduct(nums):
    n = len(nums)
    if not nums or n == 0:
        return 0
    pos_product = [0] * n
    neg_product = [0] * n
    max_product = [0] * n
    pos_product[0] = neg_product[0] = max_product[0] = nums[0]
    
    for i in range(1,n):
        a = pos_product[i-1] * nums[i]
        b = neg_product[i-1] * nums[i]
        pos_product[i] = max(max(a,b),nums[i]) 
        neg_product[i] = min(min(a,b),nums[i]) 
        max_product[i] = max(max_product[i-1],pos_product[i])
    return max_product[n-1]
    
nums = [6,-3,-10,0,2]
maxproduct(nums)



def maxproduct(nums):
    n = len(nums)
    if not nums or n == 0:
        return 0
        
    pos_product = neg_product= max_product = nums[0]
    
    for i in range(1,n):
        a = pos_product * nums[i]
        b = neg_product * nums[i]
        pos_product = max(max(a,b),nums[i]) 
        neg_product = min(min(a,b),nums[i]) 
        max_product = max(max_product,pos_product)
    return max_product
    
nums = [6,-3,-10,0,2]
maxproduct(nums)
