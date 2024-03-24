
#############################################
# 2942. Find Words Containing Character     #
#############################################

# leetcode link: https://leetcode.com/problems/find-words-containing-character/description/



class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for w in range(len(words)):
            if x in words[w]:
                result.append(w)
        return result
        