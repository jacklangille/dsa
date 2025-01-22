"""
Your LinkedList class should support the following operations:

    LinkedList() will initialize an empty linked list.
    int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    void insertHead(int val) will insert a node with val at the head of the list.
    void insertTail(int val) will insert a node with val at the tail of the list.
    bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
    int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
"""

from typing import List


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)  # Make new node
        new_node.next = (
            self.head.next
        )  # Make the new_node.next be the current head.next
        self.head.next = new_node  # Set the

        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        # Find the index of the node before the one we wish to remove
        while curr and i < index:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        output = []

        while curr:
            output.append(curr.val)
            curr = curr.next
        return output
