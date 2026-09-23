class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        #brute force approach
        squares_output = []
        for i in nums:
            square = i**2
            squares_output.append(square)
        final_res = sorted(squares_output)
        return final_res
        #Time complexity: O(N log N)
        #Space complexity: O(N)
        '''
        #binary search approach
        squares_output = []
        left, right = 0, len(nums)-1
        while left <= right:
            if (nums[left]*nums[left]) > (nums[right]*nums[right]):
                squares_output.append(nums[left]*nums[left])
                left += 1
            else:
                squares_output.append(nums[right]*nums[right])
                right -= 1
        return squares_output[::-1]

            
        