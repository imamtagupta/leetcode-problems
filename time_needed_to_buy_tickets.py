
######################################
# 2073. Time Needed to Buy Tickets   #
######################################

# leetcode link: https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count_of_seconds = 0
        tickets_to_buy = tickets[k]
        for i in range(len(tickets)):
            if(i<=k):
                count_of_seconds += min(tickets_to_buy, tickets[i])
            else:
                count_of_seconds += min(tickets_to_buy-1, tickets[i])
        return count_of_seconds