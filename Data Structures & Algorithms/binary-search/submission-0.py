class Solution:
    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid          # Return INDEX, not value
            elif nums[mid] > target:
                right = mid - 1     # Search left half
            else:
                left = mid + 1      # Search right half

        return -1                   # Target not found