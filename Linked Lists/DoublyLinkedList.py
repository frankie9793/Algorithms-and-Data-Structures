class DoublyLinkedList:

    def __init__(self):
        self.head = None:
        self.tail = None:
    
    # O(N) Time | O(1) Space
    # Algorithm: While current node is not null or current node's value is not value
    # advance to next node, return true or false depending on node is null
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
    
    # O(1) Time | O(1) Space
    # Algorithm: ** Check if node to be removed is head or tail first **
    def remove(self, nodeToRemove):
        if nodeToRemove == self.head:
            self.head = self.head.next
        if nodeToRemove == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(nodeToRemove)

    # O(N) time | O(1) Space
    # Algorithm: Traverse the LL until value is found ** Important to keep track of node to be removed**
    def removeNodeWithValues(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) Space
    # Algorithm: ** Check if it's a single node LL ** if true no-op
    # Update node to insert's next and prev first 
    # ** Check if we are inserting before the head **
    # Finally update node's prev to not lose track
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert = self.head and nodeToInsert = self.tail:
            return 
        self.remove(nodeToInsert)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) Space
    # Algorithm: Similar but reverse of insertBefore()
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else: 
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(1) time | O(1) Space
    # Algorithm: ** Check if empty LL **
    # if not empty we insert before head
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.insertBefore(self.head, node)

    # O(1) time | O(1) Space
    # Algorithm: ** Check if empty LL **
    # If not empty we insert after tail
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(P) time, P == position | O(1) Space 
    # Algorithm: ** Check if insertion is at head (i.e position == 1) ** 
    # Traverse with a counter to position, if node is none insertion is at tail, else insertion is before the node
    def insertAtPosition(self, nodeToInsert, position):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPos = 1
        while node is not None and currentPos != position:
            node = node.next
            currentPos += 1
        if node is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(node, nodeToInsert)
    
    # Helper method to remove node bindings
    # ** Check if the node to be removed's prev and next nodes are not nulls ** 
    def removeNodeBindings(self, nodeToRemove):
        if nodeToRemove.prev is not None:
            nodeToRemove.prev.next = nodeToRemove.next
        if nodeToRemove.next is not None:
            nodeToRemove.next.prev = nodeToRemove.prev
        nodeToRemove.prev = None
        nodeToRemove.next = None
    

    


