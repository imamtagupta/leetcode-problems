
############################################
# 988. Smallest String Starting From Leaf #
############################################

# leetcode link: https://leetcode.com/problems/smallest-string-starting-from-leaf/

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def get_char(n):
            return chr(97+n)

        self.paths = []
        def dfs(root, s):
            if not root.left and not root.right:
                self.paths.append(get_char(root.val)+s)
            if root.left:
                dfs(root.left, get_char(root.val)+s) 
            if root.right:
                dfs(root.right, get_char(root.val)+s)
        dfs(root, "")
        return min(self.paths)