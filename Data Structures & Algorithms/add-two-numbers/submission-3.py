# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0, None)
        curr = dummy
        carry = 0

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            curr.next = ListNode(0,None)
            if val1 + val2 + carry > 9:
                newVal = val1 + val2 + carry - 10
                curr.next.val = newVal
                carry = 1
            else:
                curr.next.val = val1 + val2 + carry
                carry = 0
            
            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return dummy.next
            
            

            


        