class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate through the 2d matrix with nested for loop O(N^2)
        # Use a dfs on each island when you meet a 1, until you find every adjacent 1
        rows, cols = len(grid), len(grid[0])
        #calculate all of the connected components through dfs
        def dfs(i, j):
            #define base case:
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1) #right
                dfs(i+1, j) #down
                dfs(i, j-1) #left
                dfs(i-1, j) #up
                
            
        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands
        
        #Time: O(M + N)
        #Space: O(M + N)





        