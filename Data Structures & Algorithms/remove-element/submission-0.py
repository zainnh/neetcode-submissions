""" nums = []
    val = int
    need to remove each instance of val from the nums array. 
    Then need to find all (num[i] != val) = k

    return k

    example nums = [1,2,3,4,5], val = 3 -> k = 4, nums = [1,2,4,5]

    if nums[i] = val, then nums[n-1]

    because there are two elements to remove, using two pointers would be optimal



    """





class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n

