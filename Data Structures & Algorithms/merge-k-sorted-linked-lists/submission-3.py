# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res

        while True:
            minNodeInd = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNodeInd == -1 or lists[minNodeInd].val > lists[i].val:
                    minNodeInd = i
            
            if  minNodeInd == -1:
                break
            
            curr.next = lists[minNodeInd]
            lists[minNodeInd] = lists[minNodeInd].next
            curr = curr.next
            curr.next = None
        
        return res.next
            
        