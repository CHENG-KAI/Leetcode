class Solution(object):
    def twoSum(self,numbers,target):
        if numbers== None or len(numbers)==0:
            return []
        l, r = 0, len(numbers)-1

        while l < r :
            Sum = numbers[l]+numbers[r]
            if Sum < target:
                l += 1
            elif Sum > target:
                r -=1
            else:
                return [l+1,r+1]

        return []

x=Solution()
print x.twoSum([2,3,4,6,8,9],12)

# https://www.youtube.com/watch?v=4PxoZP8aEiU&list=PLvHc59peqCbMXWOdXBYbQGBxTg1BOK_mg
