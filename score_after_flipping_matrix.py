
########################################
# 861. Score After Flipping Matrix     #
########################################

# leetcode link: https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Ensure leftmost bit of each row is set to 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1  # Toggle row
            
        # Step 2: Toggle columns with more 0s than 1s
        for j in range(1, n):  # Start from the second column
            count_1 = sum(grid[i][j] for i in range(m))
            if count_1 < m - count_1:  # If more 0s than 1s in this column
                for i in range(m):
                    grid[i][j] ^= 1  # Toggle column
        
        # Step 3: Calculate the score
        score = 0
        for i in range(m):
            score += int(''.join(map(str, grid[i])), 2)
        
        return score