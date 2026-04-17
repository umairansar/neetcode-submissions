# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        head = ListNode()
        temp = head

        for i in range(n):
            l = temp.next
            r = lists[i]

            while l and r:
                if l.val < r.val:
                    temp.next = l
                    l = l.next
                else:
                    temp.next = r
                    r = r.next
                temp = temp.next

            temp.next = l or r
            temp = head
        
        return head.next
                    
