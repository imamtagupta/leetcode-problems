
#################################
# 2373. Largest Local Values in a Matrix #
#################################

# leetcode link: https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []

        # Iterate over the grid, excluding the outer layer
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                # Find the maximum value in the 3x3 submatrix centered at (i, j)
                submatrix_max = max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
                row.append(submatrix_max)
            maxLocal.append(row)

        return maxLocal