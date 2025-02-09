"""
        A
       / \
      B   C
     / \   \
    D   E   F

        A
       / \
      C   B
     / \   \
    F   E   D

"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# Example Usage:
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')

inverted_root = invert_tree(root)


def invert_tree_dfs(root):
    if not root:
        return None
    stack = [root]
    
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left  # Swap children
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return root