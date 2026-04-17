# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        temp = head
        while temp:
            temp = temp.next
            sz += 1
        
        fromStart = sz - n + 1
        print(sz, n, fromStart)
        current = head
        i = 1
        prev = None
        while current:
            if i == fromStart:
                if prev:
                    prev.next = current.next
                    break
                else:
                    head = current.next
                    current.next = None
                    break
            prev = current
            current = current.next
            i += 1

        return head
        