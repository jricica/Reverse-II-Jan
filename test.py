'''
Test  of reverse method for LL. 
'''
from linked_list import Node, LinkedList
from reverse import reverse_with_stack

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")


ll = LinkedList()
print(ll)

#add nodes to ll
ll.insert_at_end(node_a)
ll.insert_at_end(node_b)
ll.insert_at_end(node_c)
ll.insert_at_end(node_d)
print(ll)

#test reverse method
ll.reverse()
print(ll)

