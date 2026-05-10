# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        
        if  length <= 2:
            return

        right = length // 2
        left = length - right

        #Split the list into right and left sub lists and reverse the right list

        leftHead = head
        rightHead = head
        while left > 0:
            rightHead = rightHead.next
            left -= 1
        
        prev = None
        curr = rightHead
        next_node = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = leftHead
        leftHead = leftHead.next
        currMerge = head
        rightHead = prev
        while leftHead is not None and rightHead is not None:
            currMerge.next = rightHead
            rightHead = rightHead.next
            currMerge =  currMerge.next 

            currMerge.next = leftHead
            leftHead = leftHead.next
            currMerge =  currMerge.next 
        
        currMerge.next = rightHead







        



        