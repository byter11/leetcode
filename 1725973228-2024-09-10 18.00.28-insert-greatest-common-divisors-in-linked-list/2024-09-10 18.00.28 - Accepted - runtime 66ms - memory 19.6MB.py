# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        return b if a == 0 else self.gcd(b % a, a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p.next:
            p.next = ListNode(self.gcd(p.val, p.next.val), p.next)
            p = p.next.next
        return head
            