
########################################
# 1992. Find All Groups of Farmland    #
########################################

# leetcode link: https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        start = []
        end = []

        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if visited[i][j] or land[i][j] == 0:
                return
            if end[0] + end[1] < i + j:
                end[:] = [i, j]
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i, j + 1)

        ans = []
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and land[i][j] == 1:
                    start = [i, j]
                    end = [i, j]
                    dfs(i, j)
                    ans.append(start + end)
        return ans