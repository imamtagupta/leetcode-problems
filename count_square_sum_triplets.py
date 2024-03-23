
########################################
# 1925. Count Square Sum Triples       #
########################################

# leetcode link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

class Solution:
    def countTriples(self, n: int) -> int:
        numbers = [i for i in range(n+1)]
        allTriples = [permutation for permutation in permutations(numbers, 3) if permutation[0]<permutation[2] and permutation[1]<permutation[2] and permutation[1]!=permutation[0]]
        sqSumTriples = 0
        for triples in allTriples:
            if (pow(triples[0], 2) + pow(triples[1], 2) == pow(triples[2], 2)):
                sqSumTriples += 1
        return sqSumTriples