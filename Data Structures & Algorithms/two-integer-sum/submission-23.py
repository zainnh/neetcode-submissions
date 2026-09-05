class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}

      if target in seen:
        return target

      for i in range (len(nums)):
        needed = target - nums[i]
        if needed in seen:
          return [seen[needed], i]
        seen[nums[i]] = i


      

#Count the elements in array
#Initialize what number is needed by target value - current element
#if that needed number is found, print index
#if not found, 

        