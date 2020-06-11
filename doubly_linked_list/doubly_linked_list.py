"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # check for empty dll
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        
        else:
            # add new node before head
            current_head = self.head
            current_head.insert_before(value)
            self.head = current_head.prev
            self.length += 1
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # check for empty dll
        if not self.head:
            return None
        
        # check for one item in dll
        if self.head is self.tail:
            single_item = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return single_item.value
        
        # remember current_head to return later
        current_head = self.head
        
        # point new head at 2nd node, set new head's prev as None
        self.head = self.head.next
        self.head.prev = None
        
        self.length -= 1
        return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # check for empty dll
        if not self.head:
            # create new node at head, point tail at head
            self.head = ListNode(value)
            self.tail = self.head
            
            self.length += 1
            
        else: 
            # remember current tail
            current_tail = self.tail
            
            # add new node after current tail
            current_tail.insert_after(value)
            
            # reset tail to be new node
            self.tail = current_tail.next
            
            # adjust previous tail's next to be new tail
            current_tail.next = self.tail
            
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # check for empty dll
        if not self.head:
            return None
        
        # check for one item in dll
        if self.head is self.tail:
            single_item = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return single_item.value
        
        # remember current tail
        current_tail = self.tail
        
        # set new tail
        self.tail = current_tail.prev
        
        # remove current tail
        current_tail.delete()
        
        self.length -= 1
        return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # check if empty dll
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
            
        # check if argument is current head already
        elif self.head is node:
            return
            
        # check if argument is current tail already
        elif self.tail is node and self.head is not node:
            # handle tail
            current_tail = self.tail
            self.tail = current_tail.prev
            current_tail.delete()
            
            # handle new head
            current_head = self.head
            current_head.insert_before(node.value)
            self.head = current_head.prev
            
        else:
            # handle current node
            node.delete()
            
            # handle new head
            current_head = self.head
            current_head.insert_before(node.value)
            self.head = current_head.prev
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # check if empty dll
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
            
        # check if argument is current head already
        elif self.head is node:
            # remove head
            self.head = self.head.next
            self.head.prev = None
            
            # set new tail
            current_tail = self.tail
            current_tail.insert_after(node.value)
            self.tail = current_tail.next
            current_tail.next = self.tail
            
        # check if argument is current tail already
        elif self.tail is node and self.head is not node:
            return
            
        else:
            # handle current node
            node.delete()
            
            # set new tail
            current_tail = self.tail
            current_tail.insert_after(node.value)
            self.tail = current_tail.next
            current_tail.next = self.tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # check for single node
        if self.head is self.tail:
            node.delete()
            self.head = None
            self.tail = None
            
            self.length = 0
        
        # check if argument is current head
        elif self.head is node:
            # remove head
            current_head = self.head
            self.head.delete()
            self.head = current_head.next
            
            self.length -= 1
            
        # check if argument is current tail
        elif self.tail is node:
            # remove tail
            current_tail = self.tail
            self.tail = current_tail.prev
            current_tail.delete()
            
            self.length -= 1
            
        else:
            # handle current node
            node.delete()
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        list_max = 0
        current_node = self.head
        
        if self.length == 0:
            return 0
        elif self.length == 1:
            return self.head.value
        else:
            while current_node is not None:
                if (current_node.value > list_max): list_max = current_node.value
                current_node = current_node.next
                
            return list_max
                
