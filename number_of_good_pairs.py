
########################################
# 1512. Number of Good Pairs      #
########################################

# leetcode link: https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def fact(self, n):
        if n < 2:
            return 1
        return n * self.fact(n-1)

    def numIdenticalPairs(self, nums: List[int]) -> int:
        twin_dict = {}
        for x in range(len(nums)):
            curr = nums[x]
            twin_dict[curr] = twin_dict.get(curr, [])
            twin_dict[curr].append(x)
        final_nCr = 0
        for x in twin_dict:
            n = len(twin_dict[x])
            if n >= 2:
                nCr = self.fact(n)/(self.fact(2)*self.fact(n-2))
                final_nCr += nCr
        return int(final_nCr)