# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current == None:
            return head
        
        next = current.next
        prev = None
        while current:
            current.next = prev
            prev = current
            current = next
            if current != None:
                next = current.next

        return prev
            