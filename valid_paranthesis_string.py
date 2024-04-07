
#################################
# 678. Valid Parenthesis String #
#################################

# leetcode link: https://leetcode.com/problems/valid-parenthesis-string/


# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         res = ""
#         stack = []
#         count_of_star = sum([1 if ele=="*" else 0 for ele in s])
#         print(count_of_star)
#         for ele in s:
#             if ele == "(":
#                 stack.append(ele)
#             if ele == ")":
#                 if len(stack) > 0:
#                     stack.pop()
#                 elif count_of_star > 0:
#                     count_of_star -=1 
#                 else:
#                     return False
#             res += ele
#         print(f" res", res, "stack length", len(stack))
#         # if len(stack)!=0:
#         #     return False
#         final_res = ""
#         stack = []
#         count_of_star = sum([ele == '*' for ele in res])
#         print(count_of_star)
#         for ele in res[::-1]:
#             if ele == ")":
#                 stack.append(ele)
#             elif ele == "(":
#                 if len(stack) > 0:
#                     stack.pop()
#                 elif count_of_star > 0:
#                     count_of_star -=1 
#                 else:
#                     return False
#         print(stack)
#         print(f" recount_of_stars", count_of_star, "stack length", len(stack))
#         return len(stack)==0 or len(stack)<=count_of_star

class Solution:
    def check(self,s,i,o,dp):
        
        if i==len(s):
            if o == 0:
                return True
            else:
                return False
            
        if dp[i][o]!=-1:
            return dp[i][o]
        if o<0 or o>len(s)//2:
            dp[i][o]= False
        elif s[i]=="(":
            dp[i][o]= self.check(s,i+1,o+1,dp)
        elif s[i]==")":
            dp[i][o]= self.check(s,i+1,o-1,dp)
        else:
            dp[i][o]= self.check(s,i+1,o+1,dp) or self.check(s,i+1,o-1,dp) or self.check(s,i+1,o,dp)
        return dp[i][o]
    def checkValidString(self, s: str) -> bool:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.check(s,0,0,dp)