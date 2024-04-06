
######################################################
# 1249. Minimum Remove to Make Valid Parentheses     #
######################################################

# leetcode link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        stack = []
        for ele in s:
            if ele == "(":
                stack.append(ele)
            if ele == ")":
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            res += ele
        final_res = ""
        stack = []
        for ele in res[::-1]:
            if ele == ")":
                stack.append(ele)
            if ele == "(":
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            final_res += ele
        return final_res[::-1]
