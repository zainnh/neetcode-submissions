class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theset = set()
        for num in nums:
            if num in theset:
                return True
            theset.add(num)
        return False