# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_ = 0

        dummy_head = ListNode(0)
        tail = dummy_head

        while l1 and l2:
            ans = l1.val + l2.val + carry
            carry = ans // 10
            sum_ = ans % 10

            node = ListNode(sum_)
            tail.next = node
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            ans = l1.val + carry
            carry = ans // 10
            sum_ = ans % 10

            node = ListNode(sum_)
            tail.next = node
            tail = tail.next
            l1 = l1.next

        while l2:
            ans = l2.val + carry
            carry = ans // 10
            sum_ = ans % 10

            node = ListNode(sum_)
            tail.next = node
            tail = tail.next
            l2 = l2.next
        
        if carry:
            node = ListNode(carry)
            tail.next = node
            tail = tail.next

        return dummy_head.next