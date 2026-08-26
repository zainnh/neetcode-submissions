class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in pair:
                return [pair[complement], i]
            pair[num] = i
