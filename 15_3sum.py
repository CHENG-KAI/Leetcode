class Solution(object):
    def threeSum(self, nums):       
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i ==0 or nums[i]!=nums[i-1]:
                l = i+1
                r = n-1
                while l < r:
                    if nums[i]+nums[l]+nums[r] == 0:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1
                    
                    elif nums[i]+nums[l]+nums[r] < 0:
                        l+=1
                    else:
                        r-=1
        res = set(tuple(row) for row in res)
        return list(list(i) for i in res)
