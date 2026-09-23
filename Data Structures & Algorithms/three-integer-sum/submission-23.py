class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue
        
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threesum = num + nums[left] + nums[right]

                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

