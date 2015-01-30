__author__ = 'andy'


from pythonds.trees.binaryTree import BinaryTree
# <editor-fold desc="buildParseTree">
'''
from pythonds.basic.stack import Stack
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for __i in fplist:
        if __i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif __i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(__i))
            parent = pStack.pop()
            currentTree = parent
        elif __i in ['+', '-', '*', '/']:
            currentTree.setRootVal(__i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif __i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
'''
# </editor-fold>

#should make sure the first character is "("
def findParMatchLoc_my(exp):
    stack = [exp[0]]
    i = 1
    while len(stack)>0:
        if(exp[i] == "("):
            stack.append(exp[i])
        elif exp[i] == ")":
            stack.pop()
        i += 1
    return i

def buildNode_my(exp1, oper, exp2):
    nodeOP = buildParseTreeMy(oper)
    nodeOP.leftChild = buildParseTreeMy(exp1)
    nodeOP.rightChild = buildParseTreeMy(exp2)
    return nodeOP

def buildParseTreeMy(exp):
    if exp==None or exp==[]:
        return None
    if len(exp)==1:
        return BinaryTree(exp[0])

    if exp[0] == '(':
        idx = findParMatchLoc_my(exp)
        exp1=exp[1:idx-1]
        if idx==len(exp):
            return buildParseTreeMy(exp1)
        else:
            oper=exp[idx:idx+1]
            exp2=exp[idx+1:]
            return buildNode_my(exp1, oper, exp2)
    else:
        return buildNode_my(exp[0:1], exp[1:2], exp[2:])

import operator
def evaluate_my(tree):
    oper = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    left = tree.leftChild
    right = tree.rightChild
    rootVal = tree.key
    if left and right:
        fn = oper[rootVal]
        return fn(evaluate_my(left), evaluate_my(right))
    else:
        return int(rootVal)

def preorder_my(tree):
    if tree == None:
        return ""
    value = preorder_my(tree.leftChild)+tree.key+preorder_my(tree.rightChild)
    if tree.leftChild != None:
        return "("+value+")"
    else:
        return value

pt = buildParseTreeMy("( ( 10 + 5 ) * 3 )".split())
print(evaluate_my(pt))
print(preorder_my(pt))
pt.postorder()  #defined and explained in the next section

