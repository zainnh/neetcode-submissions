class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #brute force approach
        squares_output = []
        for i in nums:
            square = i**2
            squares_output.append(square)
        final_res = sorted(squares_output)
        return final_res

            
        