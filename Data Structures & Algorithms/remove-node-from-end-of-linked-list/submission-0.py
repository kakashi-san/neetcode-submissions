class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail1 = head
        tail2 = head

        for _ in range(n):
            tail2 = tail2.next

        if not tail2:
            return head.next

        while tail2.next:
            tail1 = tail1.next
            tail2 = tail2.next

        tail1.next = tail1.next.next

        return head