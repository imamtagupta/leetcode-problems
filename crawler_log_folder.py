
########################################
# 1598. Crawler Log Folder   #
########################################

# leetcode link: https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for ele in logs:
            if ele.startswith(".."):
                depth = depth -1 if depth > 0 else 0
            if not ele.startswith("."):
                depth += 1
        return depth
