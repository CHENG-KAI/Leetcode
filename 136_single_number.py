from collections import Counter
def singleNumber(nums):
    c = Counter(nums)
    d = dict(c)
    for k,v in d.items():
        if v == 1:
            return k
    
nums = [1,1,2,3,3]
print singleNumber(nums)



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))- sum(nums)
