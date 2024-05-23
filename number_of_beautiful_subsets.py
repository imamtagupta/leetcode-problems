
########################################
# 2597. The Number of Beautiful Subsets  #
########################################

# leetcode link: https://leetcode.com/problems/the-number-of-beautiful-subsets/


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def total_pair(nums, K):
        
            # Initializing a map or dictionary
            mp = dict()
            cnt = 0
            for i in range(len(nums)):
                if nums[i] in mp:
                    mp[nums[i]] += 1
                else:
                    mp[nums[i]] = 1
        
            # Difference equal to zero
            if K == 0:
                for i in mp:
                    # Frequency of element is
                    # greater than one then
                    # distinct pair is possible
                    if mp[i] > 1:
                        cnt += 1
            # Difference is not equal to zero
            else:
                for i in mp:
                    # Frequency of element + k
                    # is not zero then distinct
                    #pair is possible
                    if i + K in mp:
                        cnt += 1
        
            return cnt
            

        def recursion(nums, subs, k):
            if not nums:
                if total_pair(subs, k) < 1:
                    print(subs)
                    return [subs]
                return []
            
            return recursion(nums[1:], subs+[nums[0]], k) + recursion(nums[1:], subs, k)
        

        val = recursion(nums, [], k)
        return len(val)-1
        



# GETTING TLE ERROR IN ABOVE CODE