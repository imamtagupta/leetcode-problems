
#################################
# 404. Sum of Left Leaves       #
#################################

# leetcode link: https://leetcode.com/problems/sum-of-left-leaves/

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft = False) -> int:
        if not root:
            return 0
        if not root.left and not root.right and isLeft:
            return root.val
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False) 
        