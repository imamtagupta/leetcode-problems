
###############################################
# 2486. Append Characters to String to Make Subsequence #
###############################################

# leetcode link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for ele in s:
            if i < len(t):
                if t[i] == ele:
                    i += 1
            else:
                return 0


        return len(t)-i


        