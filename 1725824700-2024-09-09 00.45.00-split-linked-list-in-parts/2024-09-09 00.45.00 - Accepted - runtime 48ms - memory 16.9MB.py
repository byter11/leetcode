# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.length(head)
        partlen = max(1, int(n / k))
        adder = n % k if n > k else 0

        # print(n, k, partlen, adder)
        c = 0
        res = [head]

        while head:
            c += 1
            if c == partlen + (adder > 0):
                nxt = head.next
                head.next = None
                head = nxt
                if head == None:
                    break
                res.append(head)
                c = 0
                curlen = partlen
                adder -= 1
            else:
                head = head.next
        
        while len(res) < k:
            res.append(None)

        return res

    def length(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l