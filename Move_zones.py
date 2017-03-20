def count(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j], nums[i] = nums[i],nums[j]
            j+=1

def count(nums):
    for i in range(0,nums.count(0)):
            nums.remove(0)
            nums.append(0)
