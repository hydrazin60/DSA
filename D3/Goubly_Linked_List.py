class Node:
    def __init__(self, data):
        self.data = data       # Store data in the node
        self.next = None       # Initialize the next node as None
        self.prev = None       # Initialize the previous node as None

# Creating nodes with data
node1 = Node(10)
node2 = Node(20)
node3 = Node(4)
node4 = Node(50)

# Linking nodes in both directions
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

# Forward traversal (head to tail)
current = node1
print("Forward traversal:")
while current is not None:
    print(current.data, end=" <=> ")
    current = current.next
print("None")  # Indicate the end of the list

# Backward traversal (tail to head)
current = node4
print("Backward traversal:")
while current is not None:
    print(current.data, end=" <=> ")
    current = current.prev
print("None")  # Indicate the start of the list
 