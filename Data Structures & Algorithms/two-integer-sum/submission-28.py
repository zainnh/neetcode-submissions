class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}

      for i in range (len(nums)):
        needed = target - nums[i]
        if needed in seen:
          return [seen[needed], i]
        else:
          seen[nums[i]] = i 

        
        
        





  

#Create hash map to keep track of targeted number
#Create for loop that counts through the amt of elements in array using len(nums).
#The i cycles through each index number until the length of the array
#Set the needed equation to find needed value
#if the needed number is in the hash, return the index values of the sum of target
        