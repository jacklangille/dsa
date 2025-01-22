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

#        1
#     2     3
#   4  5  10


# Recursive pre-order traversal Time: O(n) Space: O(n)
def pre_order(node):
    if not node:
        return

    print(node)
    pre_order(node.left)
    pre_order(node.right)


print("Pre order recursive")
pre_order(A)


# Recursive in-order traversal Time: O(n) Space: O(n)
def in_order(node):
    if not node:
        return

    pre_order(node.left)
    print(node)
    pre_order(node.right)


print("In order recursive")
in_order(A)


# Recursive post-order traversal Time: O(n) Space: O(n)
def post_order(node):
    if not node:
        return

    pre_order(node.left)
    pre_order(node.right)
    print(node)


print("Post order recursive")
post_order(A)


# Iterative pre-order traversal Time: O(n) Space: O(n)
def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)


print("Pre order iterative")
pre_order_iterative(A)


# Level order traveral (BFS) Time: O(n) Space: O(n)
from collections import deque


def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


print("Level order traversal")
level_order(A)

# Check if value exists (DFS)


def search(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)


print(search(A, 6))
print(search(A, 5))
