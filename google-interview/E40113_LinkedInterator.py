# Andy Wu
# Solutions to Google Interview Question



__author__ = 'andy'

class NodeM:
    def __init__(self, data, next=None, nest = None):
        self.data = data
        self.next = next
        self.nest = nest

#2(3(4))(5)
def createNode(str):
    if str == None or str == "":
        return None
    if str[0] != '(':
        parLoc = str.find('(')
        if(parLoc == -1):
            return NodeM(str)
        else:
            data = str[0:parLoc]; extra = str[parLoc:]
            return NodeM(data, None, createNode(extra))
    else:
        a = str[1:len(str)-1].split(")(")
        root = createNode(a[0]); p=root
        for i in range(1, len(a)):
            p.nest = createNode(a[i]); p = p.nest
        return root

#(1)->(2(3(4)))->(4(5)(6))
def createLL(exprs):
    a = exprs[1:len(exprs)-1].split(')->(')
    root = createNode(a[0]); p = root
    for i in range(1, len(a)):
        p.next = createNode(a[i]); p = p.next
    return root


def myRun():
    data = "(1)->(2(3(4)))->(4(5)(6))"
    root = createLL(data)
    for node in iterM(root):
        print(node.data, end=" ")
    return root

def iterM(node):
    p = node
    while None != p:
        yield p
        n = p.nest
        while n!=None:
            yield n
            n = n.nest
        p = p.next

root = myRun()
