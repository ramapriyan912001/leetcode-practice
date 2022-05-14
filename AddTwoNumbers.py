# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = ListNode()
        tracker = num
        carry = 0
        while l1 and l2:
            print(type(l1), type(l2))
            tracker.val = (carry + l1.val + l2.val)%10
            carry = (carry + l1.val + l2.val)//10
            l1, l2 = l1.next, l2.next
            if l1 or l2 or carry:
                tracker.next = ListNode()
            tracker = tracker.next
        if not l1:
            while l2:
                tracker.val = (l2.val + carry)%10
                carry = (l2.val + carry)//10
                l2 = l2.next
                if l2 or carry:
                    tracker.next = ListNode()
                tracker = tracker.next
        elif not l2:
            while l1:
                tracker.val = (l1.val + carry)%10
                carry = (l1.val + carry)//10
                l1 = l1.next
                if l1 or carry:
                    tracker.next = ListNode()
                tracker = tracker.next
        if carry:
            tracker.val = carry
        return num
