class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
      
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = []
        for i in (nums1):
            if i in nums2:
                nums3.append(i)
        return nums3


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
      
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return list(nums1&nums2)
        
