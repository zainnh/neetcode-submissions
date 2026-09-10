class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        orderedNums = set(nums)

        maxLength = 0

        for num in orderedNums:
            if (num - 1) not in orderedNums:
                currentLength = 1
                while num + currentLength in orderedNums:
                    currentLength += 1
                maxLength = max(maxLength, currentLength)
        return maxLength                
        