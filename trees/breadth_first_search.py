"""
Time: O(n)
Space: O(n) worst case wide tree
"""
from collections import deque

def bfs_iterative(tree):
    if not tree or not tree[0]:  
        return
    
    queue = deque([0])  # Start from root index (0)
    
    while queue:
        index = queue.popleft()  # Get the current node index
        if index >= len(tree) or tree[index] is None:
            continue  # Ignore invalid indices
        
        print(tree[index], end=" ")  # Visit node
        
        # Enqueue left then right (FIFO order)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        if left_child < len(tree):
            queue.append(left_child)
        if right_child < len(tree):
            queue.append(right_child)

tree = ['A', 'B', 'C', 'D', 'E', None, 'F']
bfs_iterative(tree)