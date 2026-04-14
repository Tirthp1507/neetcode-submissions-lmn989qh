class Solution:
    def productExceptSelf(elf,nums):
        n = len(nums)
        output = []

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            output.append(product)

        return output