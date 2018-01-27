"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visitedNode = []
    currNode = head
    while currNode is not None:
        if currNode not in visitedNode:
            visitedNode.append(currNode)
            currNode = currNode.next
        else:
            return 1
    return 0

