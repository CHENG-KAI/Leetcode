class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float('-inf')]+nums+[float('-inf')]
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and  nums[i] > nums[i+1]:
                return i-1

#O(n)


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float('-inf')]+nums+[float('-inf')]
        l = 1
        h = len(nums)-1
        while l < h:
            mid = (l+h)/2
            if nums[mid] > nums[mid+1]:
                h = mid
            
            elif nums[mid] < nums[mid+1]:
                l = mid+1
        return l-1

#Olog(n)
