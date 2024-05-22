
########################################
# 131. Palindrome Partitioning         #
########################################

# leetcode link: https://leetcode.com/problems/palindrome-partitioning/

from collections import defaultdict
from functools import cache 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def isPal(i: int, j: int):
            lo, hi = i, j
            while lo < hi:
                if s[lo] != s[hi]: return False
                lo += 1
                hi -= 1
            return True

        jumps = defaultdict(list)

        for i in range(n):
            for j in range(i, n):
                if isPal(i, j):
                    jumps[i].append(j)
        # print(jumps)
                    
        @cache
        def findPartitions(i: int = 0):
            if i == n:
                return [[]]

            ans = []
            for j in jumps[i]:
                current = s[i: j + 1]
                partitions = findPartitions(j + 1)
                for part in partitions:
                    ans.append([current] + part)
            return ans

        return findPartitions()