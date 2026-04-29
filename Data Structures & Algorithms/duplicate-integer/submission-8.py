class Solution:
        def hasDuplicate(self, nums):
                nums.sort()
                n = len(nums)
                for i in range(n-1):
                        if nums[i] == nums[i+1]:
                                return True
                        else:
                             i+=1
                return False