
########################################
# 713. Subarray Product Less Than K    #
########################################

# leetcode link: https://leetcode.com/problems/subarray-product-less-than-k/description/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0
        
        product = 1
        count = left = 0
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count