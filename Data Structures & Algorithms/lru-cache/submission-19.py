class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.keyToNode = {}
        self.num = 0
        self.capa = capacity
        self.seqHead = None
        self.seqEnd = None

    # removeNode when we reach the capacity
    def removeNode (self, node):
        # removing the only node
        if  self.seqHead == node and self.seqEnd == node:
            self.seqHead = None
            self.seqEnd = None
            return 

        # removing the node at the end
        if not node.next:
            self.seqEnd = node.prev
            node.prev.next = None
            node.prev = None
            return
        
        # removing the node at the head
        if not node.prev:
            self.seqHead = node.next
            node.next.prev = None
            node.next = None
            return
        
        # removing a regular node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
            

    # addToEnd when we add a new node
    def addToEnd(self, node):
        if self.seqHead is None and self.seqEnd is None:
            self.seqHead = node
            self.seqEnd = node
            return 
        
        self.seqEnd.next = node
        node.prev = self.seqEnd
        self.seqEnd = node
        return


    # moveToEnd when we get a node
    def moveToEnd(self, node):
        if self.seqEnd == Node:
            return

        self.removeNode(node)
        self.addToEnd(node)
        return


    def get(self, key: int) -> int:
        node = self.keyToNode.get(key)
        if node is None:
            return -1
        
        self.moveToEnd(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        existedNode = self.keyToNode.get(key)
        if existedNode is not None:
            existedNode.val = value
            self.moveToEnd(existedNode)
            return 
        
        newNode = Node(key, value)
        self.keyToNode[key] = newNode
        if self.num < self.capa:
            self.num += 1
            self.addToEnd(newNode)
            return
        
        if self.num == self.capa:
            del self.keyToNode[self.seqHead.key]
            self.removeNode(self.seqHead)
            self.addToEnd(newNode)
            return
        
        return







