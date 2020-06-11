"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
   
   If an array is used to implement the stack data structure, then the time complexity to push or pop onto the stack will be worse than if a linked list is used. A linked list will be faster because of how it allocates space for new items. However, to search through the data in a stack, it will be faster for an array than a linked list. An array has faster lookup speed because of how the processor stores nearby memory in a cache.
"""

# Array Stack
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if not self.size:
#             return None

#         self.size -= 1
#         return self.storage.pop()


# Linked List Stack
import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if not self.size:
            return None
        self.size -= 1
        return self.storage.remove_tail()
