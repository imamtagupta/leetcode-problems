
########################################
# 506. Relative Ranks    #
########################################

# leetcode link: https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_score = sorted(score, reverse=True)
        for i in range(len(sort_score)):
            scindex = score.index(sort_score[i])
            if i==0:
                score[scindex] = "Gold Medal"
            elif i==1:
                score[scindex] = "Silver Medal"            
            elif i==2:
                score[scindex] = "Bronze Medal"
            else:
                score[scindex] = str(i+1)
        return score