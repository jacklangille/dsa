# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # For each node:
        # Swap its left and right children
        # If null, return
        # Use DFS iteratively with a stack
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left = node.right
            node.right = node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
