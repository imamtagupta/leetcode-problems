
#################################
# 1281. Subtract the Product and Sum of Digits of an Integer#
#################################

# leetcode link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, digit: int) -> int:
        res1 = 0
        res2 = 1
        while (digit > 0):
            n = digit % 10
            res1 += n
            res2 *= n
            digit //= 10
        return res2 - res1