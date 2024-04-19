
########################################
# 200. Number of Islands   #
########################################

# leetcode link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def dfs(self, grid, i, j):

        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!="1"):
            return
        
        grid[i][j]=2
        self.dfs(grid,i-1,j) # UP
        self.dfs(grid,i,j+1) # RIGHT
        self.dfs(grid,i+1,j) # DOWN
        self.dfs(grid,i,j-1) # LEFT


    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    islands += 1
        return islands
