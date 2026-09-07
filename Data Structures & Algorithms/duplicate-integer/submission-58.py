class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dup = {}

        for c in nums:
            if c in dup:
                return True
            else:
                dup[c] = True 
        
        return False
