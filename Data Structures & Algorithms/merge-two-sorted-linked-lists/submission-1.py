# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        new = None
        l = list1
        r = list2
        if l.val < r.val:
            new = ListNode(l.val)
            l = l.next
        else:
            new = ListNode(r.val)
            r = r.next
        temp = new
        
        while l != None or r != None:
            if l != None and r != None:
                if l.val < r.val:
                    temp.next = ListNode(l.val)
                    l = l.next
                else:
                    temp.next = ListNode(r.val)
                    r = r.next
                temp = temp.next
            elif l != None and r == None:
                temp.next = ListNode(l.val)
                temp = temp.next
                l = l.next
            elif l == None and r != None:
                temp.next = ListNode(r.val)
                temp = temp.next
                r = r.next
        return new

        