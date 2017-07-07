from collections import Counter
def singleNumber(nums):
    c = Counter(nums)
    d = dict(c)
    for k,v in d.items():
        if v == 1:
            return k
    
nums = [1,1,2,3,3]
print singleNumber(nums)
