# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        nth_last = dummy
        for _ in range(n):
            tail = tail.next

        while tail.next:
            tail = tail.next
            nth_last = nth_last.next
        
        nth_last.next = nth_last.next.next

        return dummy.next
