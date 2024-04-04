
######################################################
# 1614. Maximum Nesting Depth of the Parentheses     #
######################################################

# leetcode link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, depth = 0, 0
        for ele in s:
            if ele == "(":
                depth += 1
                if max_depth < depth:
                    max_depth = depth
            if ele == ")":
                depth -= 1
        return max_depth
        