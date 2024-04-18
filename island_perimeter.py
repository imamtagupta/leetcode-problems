
###############################
# 463. Island Perimeter       #
###############################

# leetcode link: https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        perim = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if j-1 < 0 or grid[i][j-1] != 1:
                        perim += 1
                    if i-1 < 0 or grid[i-1][j] != 1:
                        perim += 1
                    if j+1 > col-1 or grid[i][j+1] != 1:
                        perim += 1
                    if i+1 > row-1 or grid[i+1][j] != 1:
                        perim += 1
        return perim