class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        new_list = set()

        for num in nums:
            if num in new_list:
                return True 
            new_list.add(num)
        return False