#############################################
# 41. First Missing Positive    #
#############################################

# leetcode link: https://leetcode.com/problems/first-missing-positive/description/



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_keys = {k:True for k in range(1, len(nums)+1)}
        for x in nums:
            if sorted_keys.get(x):
                sorted_keys[x] = False
        missing_pos = [x for x in sorted_keys if sorted_keys[x]]
        if len(missing_pos):
            return missing_pos[0]
        return len(nums)+1        