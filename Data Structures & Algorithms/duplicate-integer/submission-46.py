class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inlist = set()
        for num in nums:
            if num in inlist:
                return True
            inlist.add(num)
        return False