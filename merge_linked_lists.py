# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy 


        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next


        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

if __name__ == "__main__":
    # Instantiate the solution
    solution = Solution()

    # Test Case 1: Both lists are non-empty
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)

    print("Test Case 1:")
    merged = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged)

    # Test Case 2: One list is empty
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
   
    print("\nTest Case 2:")
    merged = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged)

    # Test Case 3: Both lists are empty
    list1 = create_linked_list([])
    list2 = create_linked_list([])

    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
   
    print("\nTest Case 3:")
    merged = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged)

    # Test Case 4: Lists of different lengths
    list1 = create_linked_list([1, 5, 7])
    list2 = create_linked_list([2, 3, 6, 8])

    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
   
    print("\nTest Case 4:")
    merged = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged)
