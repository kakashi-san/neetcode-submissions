# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = ListNode(0)
        dummy_head = ListNode(0)
        dummy_head.next = tail

        sum_ = 0
        carry = 0

        while l1 and l2:

            curr_sum = l1.val + l2.val + carry
            sum_ = curr_sum % 10
            carry = curr_sum // 10
            tail.next = ListNode(sum_)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr_sum = l1.val + carry
            sum_ = curr_sum % 10
            carry = curr_sum // 10
            tail.next = ListNode(sum_)
            tail = tail.next
            l1 = l1.next

        while l2:
            curr_sum = l2.val + carry
            sum_ = curr_sum % 10
            carry = curr_sum // 10
            tail.next = ListNode(sum_)
            tail = tail.next
            l2 = l2.next

        if carry:
            tail.next = ListNode(carry)
            tail = tail.next

        return dummy_head.next.next

