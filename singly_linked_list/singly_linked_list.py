"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, current_next)


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def contains(self, value):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False

        
    """Returns the highest value currently in the list"""
    def get_max(self):

        curr_node = self.head

        if curr_node is None:
            return None

        curr_max = float("-inf")
        while curr_node is not None:
            curr_max = max(curr_max, curr_node.value)
            curr_node = curr_node.next
        
        return curr_max

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        curr_tail = self.tail
        self.tail = ListNode(value, None)
        if curr_tail:
            curr_tail.next = self.tail 
        else:
            self.head = self.tail
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_head(self):
        if self.head:
            curr_head = self.head
            if curr_head.next:
                self.head = curr_head.next
            else:
                self.head = None
                self.tail = None
            self.length -= 1
            return curr_head.value
        else:
            return None