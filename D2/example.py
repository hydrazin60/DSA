##  Linked List in python
class Node:
    def __init__(self ,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1

while current is not None:
    print(current.data , end=" => ")
    current = current.next
print("None")     

# ######################################################
# # Singly Linked List
# # data Insert on first position
# class Node:
#     def __init__(self ,data):
#         self.data = data
#         self.next = None      

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)    

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

 
# new_head = Node(100)
# new_head.next = node1

# current = new_head

# while current is not None:
#     print(current.data , end=" => ")
#     current = current.next
# print("None")

###################################################################
# Insert a new node with data 200 at the end
class Node:
    def __init__(self ,data):
        self.data =  data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1
new_tail = Node(200)

while current.next is not None:
     current = current.next
current.next = new_tail

current = node1
while current is not None:
    print(current.data , end=" => ")
    current = current.next
print("None") 

##################################################
# Insert a new node with data 500 at the 3rd position
class Node:
    def __init__(self ,data):
        self.data =  data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1
position = 3
new_Data =  Node(500)

for _ in range(3 - 1):
    if current is not None:
        print(current.data)
        current = current.next

new_Data.next = current.next
current.next = new_Data

current = node1
while current is not None:
    print(current.data , end=" => ")
    current = current.next
print("None")



 