class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        consecCount = 0

        for num in nums:
            if num == 1:
                consecCount += 1
                maxCount = max(maxCount, consecCount)
            else:
                consecCount = 0

        return maxCount
                
        