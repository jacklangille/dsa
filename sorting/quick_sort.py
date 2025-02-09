"""
Explanation:
    - Pick a pivot element
    - Partition the list into two groups: smaller than pivot (left) and larger than pivot (right)
    - Recursively sort each partition

Complexity:
    - Space: Best and average: O(nlogn), worst: O(n^2) if poor choice of pivot
    - Space: O(logn)
    
When to use: When you need a fast general-purpose sorting algorithm
"""

def quick_sort(arr: list)->list:
    """
    Recursive quick sort
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # pivot = middle
     
    left = [x for x in arr if x < pivot] # Elements smaller than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot] # Elements bigger than pivot
    
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3,5,1,7,8,2,1,4,6,8,9,12,19,591,413]))



