"""
need to find maximum height between two bars, bars can be higher than another in same container but we are looking to find the maximum, so 7 , 7 , 6 would be from 7 to 6.

need to return the max square area of the container at the minimum size wall.

can do 2 pointer here, one from start one from len - 1

if left < right:
    currentArea = min(heights[left] - heights[right]) - (r - l)
    largest = max(largest, currentArea)
    if heights[left] <= heights[right]:
        right -= 1
    else:
        left += 1
return largest
    
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        largest = 0

        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            largest = max(largest, current)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return largest



        