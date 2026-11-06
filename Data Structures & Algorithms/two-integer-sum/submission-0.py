class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in seen:
                return [seen[pair],i]
            seen[num]=i
