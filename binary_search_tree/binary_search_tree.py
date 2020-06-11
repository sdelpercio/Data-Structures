import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList
from queue import Queue
from stack import Stack


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check for lesser value
        if self.value > value:
            # if left value is empty
            if (self.left is None): self.left = BSTNode(value)
                
            # if left value holds a node
            else: self.left.insert(value)
                
        # check for greater or equal value
        elif self.value <= value:
            # if right value is empty
            if (self.right is None): self.right = BSTNode(value)
                
            # if right value holds a node
            else: self.right.insert(value)        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if current value is target
        if (self.value == target): return True
    
        # if target is lesser and left node exists
        elif self.value > target and self.left: 
            return self.left.contains(target)
            
        # if target is greater and right node exists
        elif self.value <= target and self.right: 
            return self.right.contains(target)
            
        else: return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check for last node
        if (self.right is None): return self.value
        
        # if not, keep moving right
        else: return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on current value
        fn(self.value)
        
        # if right node exists, recurse
        if (self.right): self.right.for_each(fn)
        
        # if left node exists, recurse
        if (self.left): self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # only print if left node is empty
        if (node.left == None): print(node.value)
        
        # if theres a left node, recall function
        if (node.left): node.in_order_print(node.left)
        
        # handle middle values
        if (node.left and node.right): print(node.value)
        
        # if theres a right node, recall function
        if (node.right): node.in_order_print(node.right)
        
        # otherwise if right node is empty, print
        if (node.left and node.right == None): print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # initialize queue and pointer variable
        bft_queue = Queue()
        current_node = node
        bft_queue.enqueue(current_node)
        
        while bft_queue.size != 0:
            current_node = bft_queue.dequeue()
            
            print(current_node.value)
            
            if current_node.left != None:
                bft_queue.enqueue(current_node.left)
    
            if current_node.right != None:
                bft_queue.enqueue(current_node.right)     

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize stack and current node pointer
        dft_stack = Stack()
        current_node = node
        dft_stack.push(current_node)
        
        while dft_stack.size != 0:
            # grab node off stack
            current_node = dft_stack.pop()
            
            # print current_node
            print(current_node.value)
            
            if current_node.right != None:
                dft_stack.push(current_node.right)
                
            if current_node.left != None:
                dft_stack.push(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
