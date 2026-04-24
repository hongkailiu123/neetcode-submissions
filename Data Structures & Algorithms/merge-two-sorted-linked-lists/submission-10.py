# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if curr1 == None: return curr2
        if curr2 == None: return curr1
        res = None
        if curr1.val <= curr2.val:
            res = curr1
            curr1 = curr1.next
        else:
            res = curr2
            curr2 = curr2.next
        
        resCurr = res

        while curr1 or curr2:
            if curr1 == None:
                resCurr.next = curr2
                curr2 = curr2.next
                resCurr = resCurr.next
            elif curr2 == None:
                resCurr.next = curr1
                curr1 = curr1.next
                resCurr = resCurr.next
            elif curr2.val <= curr1.val:
                resCurr.next = curr2
                curr2 = curr2.next
                resCurr = resCurr.next
            else:
                resCurr.next = curr1
                curr1 = curr1.next
                resCurr = resCurr.next
        return res
            
                
        