
###############################
# 2582. Pass the Pillow     #
###############################

# leetcode link: https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = time//(n-1)
        m = time%(n-1)
        if d % 2 != 0:
            return n-m
        return m+1