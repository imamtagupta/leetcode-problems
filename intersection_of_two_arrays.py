
########################################
# 350. Intersection of Two Arrays II   #
########################################

# leetcode link: https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for ele in nums1:
            if ele in nums2:
                nums2.remove(ele)
                res.append(ele)
        return res