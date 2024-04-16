
#################################
# 623. Add One Row to Tree      #
#################################

# leetcode link: https://leetcode.com/problems/add-one-row-to-tree/description/



class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # If the target depth is 1, add a new root node with the given value
        # and set the current root as its left child
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        # If the target depth is not 1, call the dfs method to traverse the tree
        self.dfs(root, val, depth, 1)
        return root

    def dfs(self, node, val, depth, current_depth):
        # Base case: if the current node is None, return
        if not node:
            return

        # If we've reached the depth just before the target depth,
        # add new nodes with the given value as left and right children of the current node
        if current_depth == depth - 1:
            left_node = TreeNode(val)
            right_node = TreeNode(val)
            left_node.left = node.left
            right_node.right = node.right
            node.left = left_node
            node.right = right_node
            return

        # Continue the depth-first traversal to the left and right children
        self.dfs(node.left, val, depth, current_depth + 1)
        self.dfs(node.right, val, depth, current_depth + 1)