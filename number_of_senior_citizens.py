
######################################
# 2678. Number of Senior Citizens  #
######################################

# leetcode link: https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for d in details:
            if int(d[11:13]) > 60:
                counter += 1
        return counter
