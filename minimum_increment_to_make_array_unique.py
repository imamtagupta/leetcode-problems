
########################################
# 945. Minimum Increment to Make Array Unique   #
########################################

# leetcode link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        minIncreament = 0

        for i in range(1, len(nums)):
            # Ensure each element is greater than its previous
            if nums[i] <= nums[i - 1]:
                # Add the required increment to minIncrements
                increment = nums[i - 1] + 1 - nums[i]
                minIncreament += increment

                # Set the element to be greater than its previous
                nums[i] = nums[i - 1] + 1
        return minIncreament