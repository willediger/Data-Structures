from doubly_linked_list import DoublyLinkedList


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   -- The difference is the underlying data structure. The array will perform better I would guess
   because we are never adding or removing elements to the middle of the queue, which is one of the
   advantages of linked lists.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

########################
# ARRAY IMPLEMENTATION #
########################
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0,value)

#     def dequeue(self):
#         if len(self):
#             return self.storage.pop()
#         else:
#             return None


######################
# DLL IMPLEMENTATION #
######################
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if len(self):
            return self.storage.remove_from_tail()
        else:
            return None
