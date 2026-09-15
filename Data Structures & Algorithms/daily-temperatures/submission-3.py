class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                temp, position = stack.pop()
                ans[position] = i - position
            stack.append((j, i))
        return ans
        