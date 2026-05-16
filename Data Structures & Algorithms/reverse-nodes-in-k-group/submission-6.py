# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse the next k nodes including cur, returning true if enough nodes
        res = ListNode(0, head)
        cur = res
        def reverseKNodes(cur) -> Optional[ListNode]:
            firstNode = cur.next
            if firstNode is None:
                return None
            h = firstNode
            t = firstNode
            for _ in range(k - 1):
                t = t.next
                if t is None:
                    return None
            # we have enough nodes
            prev = None
            curNode = firstNode
            nxt = None
            for _ in range(k):
                nxt = curNode.next
                curNode.next = prev
                prev = curNode
                curNode = nxt
            h.next = nxt
            cur.next = t

            return h
    
        while True:
            cur = reverseKNodes(cur)
            if cur is None:
                return res.next
                

            




        