class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def __str__(self):
        return str(self.val)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# Traverse tree pre order recursive
def pre_order(node):
    if not node:
        return

    print(node)    
    pre_order(node.left)
    pre_order(node.right)
print("PRE ORDER")
pre_order(A)


# Traverse tree in order recursive
def in_order(node):
    if not node:
        return

    pre_order(node.left)
    print(node)    
    pre_order(node.right)
print("IN ORDER")
in_order(A)

# Traverse tree post order recursive
def post_order(node):
    if not node:
        return 

    post_order(node.left)
    post_order(node.right)
    print(node)    
print("POST ORDER")
post_order(A)

from collections import deque
# Traverse tree level order iterative
def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft() # fetch the left most node for this level 
        print(node) # visit the node

        if node.left: 
            q.append(node.left)
        if node.right:
            q.append(node.right)

print("LEVEL ORDER")
level_order(A)

# DFS search
def dfs():
    pass

# BFS search
def bfs():
    pass

# Invert
def invert():
    pass

