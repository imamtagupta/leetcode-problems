
########################################
# 1662. Check If Two String Arrays are Equivalent   #
########################################

# leetcode link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sum_word1 = "".join(word1)
        sum_word2 = "".join(word2)
        return sum_word1 == sum_word2
        