import bisect
def findClosestElements(arr, k, x):  
    l=r = bisect.bisect_left(arr,x)
    while r-l < k:
        if r == len(arr):return arr[-k:]
        elif l == 0:return arr[:k]
        elif abs(x-arr[l-1]) <= abs(arr[r]-x):l-=1
        else: r+=1
    return arr[l:r]
        
            
        
    
    
    
arr = [0,1,2,2,2,3,6,8,8,9]
findClosestElements(arr, 5,9)

