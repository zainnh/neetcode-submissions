class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {}

        for i, num in enumerate(nums):
          complement = target - num
          
          if complement in PrevMap:
            return[PrevMap[complement], i]
        
          PrevMap[num] = i