""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    
    if root is None:
        return True
    
    def isBST(node, min, max):
        
            
        if node.data <= min:
            return False

        if node.data >= max:
            return False

        checkLeft = True
        checkRight = True

        if node.left is not None:
            checkLeft = isBST(node.left, min, node.data)
        if node.right is not None:
            checkRight = isBST(node.right, node.data, max)

        return checkLeft and checkRight



    return isBST(root, float('-inf'), float('inf'))