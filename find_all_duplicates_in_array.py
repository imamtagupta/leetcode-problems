

###########################################
# 442. Find All Duplicates in an Array    #
###########################################

# leetcode link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupl = {}
        res = []
        for num in nums:
            if dupl.get(num):
                res.append(num)
            else:
                dupl[num] = 1
        return res