
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
    

# A better time complexity similar solution:

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, path: str):
            nonlocal ans
            path = path + str(node.val)
            if not node.left and not node.right:
                ans += int(path)
            else:
                if node.left: dfs(node.left, path)
                if node.right: dfs(node.right, path)
        dfs(root, "")
        return ans