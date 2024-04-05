
########################################
# 1544. Make The String Great   #
########################################

# leetcode link: https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        sList = list(s)
        sList.append(' ')
        goodList = []
        i=0
        while i<len(sList)-1:
            diff = abs(ord(sList[i]) - ord(sList[i+1]))
            if diff==32:
                sList = sList[:i] + sList[i+2:]
                i = 0
                goodList = []
                continue
            else:
                goodList.append(sList[i])
            i+=1
        return ''.join(goodList)