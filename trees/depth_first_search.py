"""
        A
       / \
      B   C
     / \   \
    D   E   F

tree = ['A', 'B', 'C', 'D', 'E', None, 'F']
Time: O(n)
Space: O(n) worst case skewed tree, O(logn) best case balanced tree
"""        


def dfs_iterative(tree):
    if not tree or not tree[0]:
        return 
    
    stack = [0] # Start at root index 0

    while stack:
        index = stack.pop()
        
        if index >= len(tree) or tree[index] is None:
            continue  # Ignore invalid indices
        
        print(tree[index], end=" ") # visit node

        # push right child first so left is processed first 
        right_child = 2 * index + 2 # Get index of right child
        left_child = 2 * index + 1 # Get index of left child
        
        if right_child < len(tree):  # Ensure index is in bounds
            stack.append(right_child)
        if left_child < len(tree):  # Ensure index is in bounds
            stack.append(left_child)




# Example Run
tree = ['A', 'B', 'C', 'D', 'E', None, 'F']
dfs_iterative(tree)
