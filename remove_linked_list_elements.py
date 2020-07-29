# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        h = head
        c = head
        while c.val == val:
            c = c.next
            h = c
            if c == None:
                return None

        while c.next != None:
            if c.next.val == val:
                c.next = c.next.next
            else:
                c = c.next

        return h
