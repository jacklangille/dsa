# DURATION: 45 MINS

# Q1: Implement a hashmap with insert, remove and get methods
class HashMap:
    def __init__(self, size) -> None:
        self.size = size
        self.buckets = [[] for _ in size]

    def _hash(self, k):
        return hash(k) % self.size

    def insert(self, k, v):
        idx = self._hash(k)
        bucket = self.buckets[idx]

        for i, (key,_) in enumerate(bucket):
            if k == key:
                bucket[i] = (k,v)
                return
        bucket.append((k,v))
    
    def remove(self,k):
        idx = self._hash(k)
        bucket = self.buckets[idx]

        for i, (key,_) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
        return None 


    def get(self,k):
        idx = self._hash(k)
        bucket = self.buckets[idx]

        for _, (key,val) in enumerate(bucket):
            if k == key:
                return val
        return None 

# Q2: Given the following binary tree, implement pre-order, in-order, post-order traversal. 
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

# Pre order
def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

# In order
def in_order(root):
    if root:
        pre_order(root.left)
        print(root.val)
        pre_order(root.right)

# Post order
def post_order(root):
    if root:
        pre_order(root.left)
        pre_order(root.right)
        print(root.val)

# Q3: Given the following binary tree, create a depth first search function that searches for a given target, x.
def dfs_search_iterative(root, target):
    if root is None:
        return False

    stack = [root]  # Start with the root node

    while stack:
        node = stack.pop()  # Process node

        if node.val == target:
            return True  # Found the target

        # Push right first so left is processed first (LIFO order)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return False  # Target not found

print(dfs_search_iterative(A, 5))  # True
print(dfs_search_iterative(A, 20)) # False

# Q4: Given the following binary tree, create a breadth first search function that searches for a given target, x.
from collections import deque

def bfs_search_iterative(root, target):
    if root is None:
        return False

    queue = deque([root])  # Initialize queue with root

    while queue:
        node = queue.popleft()  # Dequeue the first element

        print(node.val)  # Process node
        if node.val == target:
            return True  # Found the target

        # Enqueue left first, then right (FIFO order)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False  # Target not found
