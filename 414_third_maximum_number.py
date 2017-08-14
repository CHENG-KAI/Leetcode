class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()
        a = list(set(nums))
        a.sort()
        if len(a) <= 2:
            return max(a)
        else:
            return a[-3]
