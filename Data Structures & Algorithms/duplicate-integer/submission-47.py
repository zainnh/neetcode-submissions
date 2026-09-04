class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {};

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True

                

        return False;

        
#Create hash map to save numbers to
#Run a loop through the array
#