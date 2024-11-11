###### Assignment linkedlist Q)1 Define a class Node to Describe a node of a singly Linked List

class Node:
    def __init__(self , item =None , next = None):
        self.item = item
        self.next = next

### item: This holds the actual data of the node, and it defaults to None, allowing the creation of an empty node if needed.
### next: This is the reference to the next node in the linked list. By default, it's None, meaning the node is initially not linked to any other node until you explicitly link it.










###########3 Assignment linkedlist Q2)  Define a class SLL to impplement singly Linked List with __init--() method to create and initialise star refrence variable.


class Node:
    def __init__(self , item =None , next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self , start = None):
        self.start = start       
    def is_empty(self):
        return self.start is None


 