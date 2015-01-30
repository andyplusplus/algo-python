__author__ = 'andy'

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isEqual(n1, n2):
    if n1==None and n2==None:
        return True
    if n1==None or n2==None:
        return False
    if n1.val != n2.val:
        return False
    if isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right):
        return True
    elif isEqual(n1.left, n2.right) and isEqual(n1.right, n2.left):
        return True
    else:
        return False