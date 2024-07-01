#############################################
# 1550. Three Consecutive Odds              #
#############################################

# leetcode link: https://leetcode.com/problems/three-consecutive-odds/


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for ele in arr:
            if ele % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return count >= 3