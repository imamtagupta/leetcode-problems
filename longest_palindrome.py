
######################################################
# 409. Longest Palindrome                            #
######################################################

# leetcode link: https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = {}
        for ele in s:
            map[ele] = map.get(ele, 0) + 1
        n = len(s)
        odds = 0
        for i in map:
            if map[i] % 2 != 0:
                odds +=1
        if odds >= 1:
            return n-odds+1
        return n
        