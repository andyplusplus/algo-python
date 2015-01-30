__author__ = 'andy'

class Node:
    def __init__(self, key, value=None, le=None, ri=None, N=1):
        self.key = key
        self.value = value
        self.le = le
        self.ri = ri
        self.N = N

class BST:
    def __init__(self):
        self.root = None

    def size(self, node=None):
        if not node: node = self.root
        return None

    # return value associated with key in the subtree
    # return null if not present
    def get(self, key, node=None):
        node = self.getNode(key, node)
        if node: return node.value
        else: return node

    def getNode(self, key, node=None):
        if not node: node = self.root
        while not node==None:
            if node.key==key: break
            elif key<node.key: node = node.le
            else: node = node.ri
        return node

    def putroot(self, key, value=None):
        self.root = self.put(self.root, key, value)

    def put(self, node, key, value=None):
        if not node:
            return Node(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.le = self.put(node.le, key, value)
        else:
            node.ri = self.put(node.ri, key, value)
        return node

    def __str__(self):
        return self.__tostr(self.root)

    def __tostr(self, node):
        if not node:
            return ""
        return "%s %d %s" % (self.__tostr(node.le), node.key, self.__tostr(node.ri))

    #return minimum key
    def minRoot(self):
        return self.min(self.root)
    def min(self, node):
        while node.le:
            node = node.le
        return node.key

    #return node with root value
    def floorRoot(self, key):
        self.floor(key, self.root)
    def floor(self, key, node):
        if not node: return None
        if key == node.key: return node
        elif key<node.key: return self.floor(key, node.le)
        else: #key>node.key
            if node.ri and node.ri.value>key: return node
            else: self.floor(key, node.ri)

    def select(self, k):
        pass

    def selectNode(self, node, k): #409
        pass

    def rank(self, key, node=Null):#409
        pass

    def deleteMinRoot(self):
        pass

    def deleteMin(self, x):
        pass

    def deleteKey(self, key):
        pass

    def keys(self):
        pass

    def keysInRange(self, lo, hi):
        pass

    def keysInRangeForNode(self, lo, hi):#413
        pass


from unittest import TestCase
import sort.SortUtil
class Test_BST(TestCase): #p409
    def setUp(self):
        a = sort.SortUtil.getArrayM(30)
        self.bst = BST()
        for i in a: self.bst.putroot(i, 2*i)

    def testRun(self):
        print(self.bst)

    def testFun(self):
        self.assertTrue(self.bst.minRoot()==0)


