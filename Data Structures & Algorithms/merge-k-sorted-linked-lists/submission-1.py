# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiniAmongLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        smallestStartItem = float('inf')
        nodeToReturn = None
        listIndex = -1
        for i in range(len(lists)):
            if lists[i] and lists[i].val < smallestStartItem:
                listIndex = i
                smallestStartItem = lists[i].val
                nodeToReturn = lists[i]
        if nodeToReturn:
            lists[listIndex] = lists[listIndex].next
            nodeToReturn.next = None
        
        return nodeToReturn
    
    def moreNodeToMerge(self, mergeListIndex, lists: List[Optional[ListNode]]) -> bool:
        for i in range(len(lists)):
            if i != mergeListIndex and lists[i] is not None:
                return True
        
        return False


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numLists = len(lists)
        mergeListIndex = -1
        if numLists == 0:
            return None
        
        smallestStartItem = float('inf')
        for i in range(numLists):
            if lists[i].val < smallestStartItem:
                smallestStartItem = lists[i].val
                mergeListIndex = i
        
        #We found the smallest start item and list
        resHead = lists[mergeListIndex]
        lists[mergeListIndex] = resHead.next
        resCurr = resHead

        while self.moreNodeToMerge(mergeListIndex, lists):
            node = self.findMiniAmongLists(lists)
            if resCurr.next != node:
                node.next = resCurr.next
                resCurr.next = node
            resCurr = resCurr.next
        
        return resHead












        
        