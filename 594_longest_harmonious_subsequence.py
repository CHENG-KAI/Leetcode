class Solution(object):
    import collections
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        a = dict(collections.Counter(nums))
        res = []
        for i in a:
            if i+1 in a: res.append(a[i+1] +a[i])
            else:res.append(0)
        return max(res)
