
########################################
# 1971. Find if Path Exists in Graph          #
########################################

# leetcode link: https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n <= 1:
            return True
        visited = [False] * n
        q = []
        q.append(source)
        visited[source] = True
        while q:
            data = q.pop(0)
            for i in range(len(edges)):
                edge = edges[i]
                if (edge == [data, destination]) or (edge == [destination, data]):
                    return True
                if data in edge: 
                    nextVal = edge[0] if edge[1]==data else edge[1]
                    if not visited[nextVal]:
                        q.append(nextVal)
                        visited[nextVal] = True
        return False
                    
                