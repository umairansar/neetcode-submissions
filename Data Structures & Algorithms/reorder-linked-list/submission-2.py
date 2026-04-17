# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find length of list
        ctr = 1
        temp = head
        while temp:
            temp = temp.next
            ctr += 1
        
        # Place l and r at start of two sublists
        mid = ctr // 2
        i = 1
        temp = head
        l = head
        while i <= ctr:
            if i == mid:
                r = temp.next #start r sublist
                temp.next = None #end l sublist
                break
            temp = temp.next
            i += 1

        print("Left sublist:")
        self.printList(l)
        print("Right sublist:")
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

        print("Right sublist (reversed):")
        self.printList(r)

        head = l
        currentL = l
        # nextL = currentL.next
        currentR = r
        # nextR = currentR.next
        while currentL and currentR:
            nextL = currentL.next
            nextR = currentR.next
            currentL.next = currentR
            currentR.next = nextL
            currentL = nextL
            currentR = nextR
        
        print("result:")
        self.printList(head)
        # return head

    def printList(self, head: Optional[ListNode]) -> None:
        temp = head
        while temp:
            print(temp.val, end=", ")
            temp = temp.next
        print("")
        # r