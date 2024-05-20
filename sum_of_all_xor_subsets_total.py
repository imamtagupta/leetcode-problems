
########################################
# 1863. Sum of All Subset XOR Totals   #
########################################

# leetcode link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/


class Solution:
    def xor_of_array(self, arr):
        if not arr:
            return 0
        val = arr[0]
        for ele in arr[1:]:
            val ^= ele
        return val

    def subseq(self, p, un, sums):
        if not un:
            # print(p)
            sums += self.xor_of_array(p)
            return sums
        sums = self.subseq(p+[un[0]], un[1:], sums)
        sums = self.subseq(p, un[1:], sums)
        return sums


    def subsetXORSum(self, nums: List[int]) -> int:
        return self.subseq([], nums, 0)