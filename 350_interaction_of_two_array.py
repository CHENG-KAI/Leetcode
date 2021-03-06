def intersect(nums1, nums2):
    nums3 = []
    for i in nums2:
        if i in nums1:
            nums3.append(i)
            nums1.remove(i)
    return nums3
            

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = dict()
        res = []
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in nums2:
            if i in dict1 and dict1[i]>0:
                res.append(i)
                dict1[i] -= 1
        return res
