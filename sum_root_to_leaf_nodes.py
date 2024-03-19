
#################################
# 129. Sum Root to Leaf Numbers #
#################################

# leetcode link: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], sum=0) -> int:
        if not root: 
            return 0
        sum = (sum *10 ) + root.val  
        if not root.left and not root.right:
            return sum
        return self.sumNumbers(root.left, sum) + self.sumNumbers(root.right, sum)