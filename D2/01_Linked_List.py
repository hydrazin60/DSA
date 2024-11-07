#######singly linked list

############ Normal singly linked list #####
class Node:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.next = None  # Initialize the next node as None

# Creating nodes with data
node1 = Node(10)
node2 = Node(20)
node3 = Node(4)
node4 = Node(50)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Traversing and printing the linked list
current = node1
while current is not None:
    print(current.data, end=" => ")
    current = current.next
print("None")  # Indicate the end of the list
 
 
############ data Insert on first position########
class Node:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.next = None  # Initialize the next node as None

# Creating nodes with data
node1 = Node(10)
node2 = Node(20)
node3 = Node(4)
node4 = Node(50)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Adding a new node with data 60 at the beginning
new_head = Node(60)
new_head.next = node1  # Link the new head to the current head (node1)

# Now the head of the list is new_head
current = new_head
while current is not None:
    print(current.data, end=" => ")
    current = current.next
print("None")  # Indicate the end of the list


############ data insert last position and  any position###
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes with data
node1 = Node(60)  # Adding 60 as the first node
node2 = Node(10)
node3 = Node(20)
node4 = Node(4)
node5 = Node(50)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Insert 100 at the 4th position (between 20 and 4)
new_node_100 = Node(100)
current = node1
position = 3  # Target position for insertion (0-based index: after node3)

# Traverse to the node before the target position
for _ in range(position - 1):
    if current is not None:
        current = current.next

# Insert the new node
new_node_100.next = current.next
current.next = new_node_100

# Insert 200 at the end
new_node_200 = Node(200)
current = node1

# Traverse to the end of the list
while current.next is not None:
    current = current.next

# Link the last node to the new node
current.next = new_node_200

# Traversing and printing the updated linked list
current = node1
while current is not None:
    print(current.data, end=" => ")
    current = current.next
print("None")  # Indicate the end of the list
