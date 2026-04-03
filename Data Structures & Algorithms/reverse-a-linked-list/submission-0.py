# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # None  <-  0    ->   1  -> 2
        # prev  -> curr  -> next
        # prev  <- curr     next -> 
        curr = head
        # print(curr.next.val)
        while curr != None:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        return prev


            

