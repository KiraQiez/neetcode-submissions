class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Pass 1: res[i] = product of all elements LEFT of i
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # Pass 2: multiply by product of all elements RIGHT of i
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res