# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            head = ListNode()
            temp = head

            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next

            temp.next = l1 or l2
            return head.next

        while len(lists) > 1:
            print(len(lists))
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            res = merge(l1, l2)
            lists.append(res)

        return lists[0] if lists else None
            