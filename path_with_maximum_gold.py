
########################################
# 1219. Path with Maximum Gold    #
########################################

# leetcode link: https://leetcode.com/problems/path-with-maximum-gold/
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid, visited):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                return 0
            
            visited[i][j] = True
            current_gold = grid[i][j]
            max_gold = 0
            
            # Explore adjacent cells
            for dx, dy in directions:
                max_gold = max(max_gold, dfs(i + dx, j + dy, grid, visited))
            
            visited[i][j] = False  # Backtrack
            return current_gold + max_gold
        
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = [[False] * n for _ in range(m)]  # Initialize visited matrix for each start position
                    max_gold = max(max_gold, dfs(i, j, grid, visited))
        
        return max_gold