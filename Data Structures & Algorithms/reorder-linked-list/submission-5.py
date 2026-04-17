# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find length of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l = head
        r = slow.next

        slow.next = None
        self.printList(l)
        self.printList(r)

        #Flip the right sublist
        current = r
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        r = prev

        head = l
        currentL = l
        currentR = r
        while currentL and currentR:
            nextL = currentL.next
            nextR = currentR.next
            currentL.next = currentR
            currentR.next = nextL
            currentL = nextL
            currentR = nextR
        
    def printList(self, head: Optional[ListNode]) -> None:
        temp = head
        while temp:
            print(temp.val, end=", ")
            temp = temp.next
        print("")
        # r