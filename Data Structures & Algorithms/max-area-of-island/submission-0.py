class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        #perform dfs to find all connected components (connected 1's that form an island)
        def dfs(i, j):
            #maxArea = 0
            #set base case:
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))
            
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea



        