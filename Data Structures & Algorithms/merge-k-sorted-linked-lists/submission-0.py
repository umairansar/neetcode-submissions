# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = list(filter(lambda x: x != None, lists))
        length = len(lists)
        ptrs = [None] * length
        for i in range(length):
            ptrs[i] = lists[i]

        nulls = 0
        head = ListNode()
        temp = head
        while nulls < length:
            i_ptrs = list(enumerate(ptrs))
            valids = list(filter(lambda x: x[1] != None, i_ptrs))
            i_ptr, ptr = min(valids, key=lambda x: x[1].val)
            temp.next = ptr
            ptrs[i_ptr] = ptrs[i_ptr].next
            if ptrs[i_ptr] == None:
                nulls += 1
            temp = temp.next
        
        return head.next
