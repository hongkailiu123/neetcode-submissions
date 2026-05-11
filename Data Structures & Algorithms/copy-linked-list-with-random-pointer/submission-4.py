"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        nodeToIndexMap = {}
        newNodeArray = []

        curr = head
        n = 0
        while curr:
            newNode = Node(curr.val)
            newNodeArray.append(newNode)
            nodeToIndexMap[curr] = n
            n += 1
            curr = curr.next
        
        newList = newNodeArray[0]
        j = 0
        newCurr = newList
        curr2 = head
        while curr2:
            if curr2.random == None:
                newCurr.random = None
            else:
                ranIndex = nodeToIndexMap[curr2.random]
                newCurr.random = newNodeArray[ranIndex]
            newCurr.next = newNodeArray[j+1] if j+1 < n else None
            j += 1
            newCurr = newCurr.next
            curr2 = curr2.next
        
        return newList


            



