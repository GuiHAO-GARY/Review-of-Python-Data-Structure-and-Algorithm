import operator
import re
from Basic_Data_Structure import Stack


# ---------------- List of list expression -------------------
def BinaryTree(r):
    """
    Create one binary tree with 2 null list node
    :param r: Value stored in root node
    :return: binary tree
    """
    return [r, [], []]


def insertLeft(root, newBranch):
    """
    Insert a new branch to left child tree
    :param root: above binary tree (one root and 2 null node)
    :param newBranch: A child tree
    :return: Whole tree
    """
    t = root.pop(1)  # Left child tree list
    if len(t) > 1:  # Left child tree has elements
        root.insert(1, [newBranch, t, []])  # Treat newBranch as new left node and insert it between root and t.
    elif len(t) == 0:
        root.insert(1, [newBranch, [], []])  # Treat newBranch as left node
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


# Create a binary tree without left child and right child
r = BinaryTree(3)

# Insert nodes into tree
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)

# get child tree
l = getLeftChild(r)
getRightChild(r)

# get root value
getRootVal(r)

# set root value
setRootVal(l, 9)
r

# insert nodes to child tree
insertLeft(l, 11)
r

# embedding
getRightChild(getRightChild(r))


# ------------ Class expression ---------------
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.getLeftChild().preorder()
        if self.rightChild:
            self.getRightChild().preorder()


r = BinaryTree('a')
r.getRootVal()

print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('Hello')
print(r.getRightChild().getRootVal())
r.insertLeft('d')
print(r.getLeftChild().getRootVal())


##############################################
class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = BinaryTree(10)
b = BinaryTree(5)
c = BinaryTree(15)
d = BinaryTree(3)
e = BinaryTree(7)
f = BinaryTree(12)
g = BinaryTree(14)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


def findMin(root):
    if root.right:
        current = root.right
        while current.left:
            current = current.left
        return current.val


def findMax(root):
    if root.left:
        current = root.left
        while current.right:
            current = current.right
        return current.val


def IfBinarySearchTree(root):
    indicator = True
    if root:
        stack = [root]
        while len(stack) > 0 and indicator:
            current = stack.pop()
            if current.left:
                left_max = findMax(current)
                if left_max < current.val:
                    stack.append(current.left)
                else:
                    indicator = False
            if current.right:
                right_min = findMin(current)
                if right_min > current.val:
                    stack.append(current.right)
                else:
                    indicator = False
    return indicator


IfBinarySearchTree(a)


# Create parse tree
# Toolkit stack
# homework 1, 2: handle blank, and, or, not logical operator
def split_expression(fpexp):
    # split data according to some patterns
    patterns = '(\()|(\))|(\+)|(\-)|(\/)|(\*)|(and)|(or)|(not)| '
    split_list = re.split(patterns, fpexp)
    split_list = [i for i in split_list if i is not None and i != '']
    return split_list


def buildParseTree(fpexp):
    fplist = split_expression(fpexp)
    temp_stack = Stack()
    eTree = BinaryTree('unsetting')
    temp_stack.push(eTree)
    current_node = eTree
    for string in fplist:
        if string == '(':
            current_node.insertLeft('unsetting')
            temp_stack.push(current_node)
            current_node = current_node.getLeftChild()
        elif string in ['+', '-', '/', '*', 'and', 'or']:
            current_node.setRootVal(string)
            current_node.insertRight('unsetting')
            temp_stack.push(current_node)
            current_node = current_node.getRightChild()
        elif string == 'not':
            current_node = temp_stack.pop()
            current_node.setRootVal(string)
            current_node.leftChild = None
            current_node.insertRight('unsetting')
            temp_stack.push(current_node)
            current_node = current_node.getRightChild()
        elif string.isnumeric():
            current_node.setRootVal(eval(string))
            current_node = temp_stack.pop()
        elif string == ')':
            current_node = temp_stack.pop()
        else:
            raise ValueError('Unknown Operator:' + string)
    return eTree


# try
b = buildParseTree('(7 + (7 or (not(8 * 5))))')


# Evaluate (calculate the parse tree)
def and_operator(a, b):
    return a and b


def or_operator(a, b):
    return a or b


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv,
             'and': and_operator, 'or': or_operator,
             'not': operator.not_}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    elif not leftC and rightC:
        return float(opers['not'](evaluate(rightC)))
    else:
        return parseTree.getRootVal()


# Try
parsetree = buildParseTree('((7 and 9) + (15 or (not(8 * 5))))')
evaluate(parsetree)


# Traversal
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# Try
preorder(parsetree)


def postorder(tree):
    if tree:
        postorder(tree.getRightChild())
        postorder(tree.getLeftChild())
        print(tree.getRootVal())


# Try
postorder(parsetree)


def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def show(root, List):
    if root:
        show(root.left, List)
        List.append(root.val)
        show(root.right, List)


# Delete redundant bracket
def printexp(tree):
    sVal = ''
    if tree:
        if tree.getRootVal() not in ['+', '-', '*', '/', 'and', 'or', 'not']:
            sVal = printexp(tree.getLeftChild())
        else:
            sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + ' ' + str(tree.getRootVal())
        if tree.getRootVal() not in ['+', '-', '*', '/', 'and', 'or', 'not']:
            sVal = sVal + printexp(tree.getRightChild())
        else:
            sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal


# Try
parsetree = buildParseTree('((7 and 9) + (15 or (not(8 * 5))))')
printexp(parsetree)


# Create binary heap and priority queue
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]  # 0 is set for using exact division in subsequent steps
        self.currentSize = 0
        self.limit = 5  # 6 limit the size of Heap

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        if self.currentSize == self.limit:
            i = self.limit // 2 + 1
            maxValue = self.heapList[i]
            maxValueIndex = i
            while i < self.limit:
                i += 1
                if self.heapList[i] > maxValue:
                    maxValue = self.heapList[i]
                    maxValueIndex = i
            self.heapList[maxValueIndex] = k
            self.percUp(maxValueIndex)
        elif self.currentSize < self.limit:
            self.heapList.append(k)
            self.currentSize += 1
            self.percUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        """
        Change the value down to the right place
        :param i: value at position i
        :return: None. Just change the value at position i to the right place and adjust positions of other elements
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def delMin(self):
        retval = self.heapList[1]  # Minimum value
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2  # i + 1, i + 2 ... are all leaf nodes
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        while i > 0:  # so these nodes i all have child nodes
            self.percDown(i)
            i = i - 1

    def heapSort(self, alist):
        self.buildHeap(alist)
        ordered_list = []
        while self.currentSize >= 1:
            ordered_list.append(self.delMin())
        return ordered_list


b = BinaryHeap()
b.insert(4)
b.insert(9)
b.insert(2)
b.insert(6)
b.insert(10)
b.heapList
b.insert(3)
b.heapList
b.delMin()
b.delMin()

c = BinaryHeap()
c.buildHeap([4, 9, 2, 6, 10])
c.heapList

d = BinaryHeap()
d.buildHeap([9, 6, 4, 2, 5])
d.heapList

# Sort by binary heap
d.heapSort([9, 6, 4, 2, 5, 11, 29, 15])


# 10. Max heap
class BinaryHeapMax:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        """
        Change the value down to the right place
        :param i: value at position i
        :return: None. Just change the value at position i to the right place and adjust positions of other elements
        """
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def delMax(self):
        retval = self.heapList[1]  # Minimum value
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2  # i + 1, i + 2 ... are all leaf nodes
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        while i > 0:  # so these nodes i all have child nodes
            self.percDown(i)
            i = i - 1


e = BinaryHeapMax()
e.buildHeap([9, 6, 4, 2, 5])
e.heapList
e.delMax()
e.heapList


# priorityQueue
class PriorityQueue(BinaryHeap):
    def __init__(self):
        super(PriorityQueue, self).__init__()
        self.limit = 10

    def enqueue(self, k):
        return self.insert()

    def dequeue(self):
        return self.delMin()


# Try
queue1 = PriorityQueue()
queue1.insert(5)
queue1.insert(4)
queue1.insert(15)
queue1.insert(29)
queue1.insert(3)
queue1.heapList
queue1.insert(6)
queue1.heapList

queue1.dequeue()
queue1.heapList


# Create binary search tree
class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0
        self.Successor = None

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:  # When the root is available
            self._put(key, val, self.root)  # Calling a recursive put method
        else:  # When the root is None
            self.root = TreeNode(key, val)  # Create a tree node at root
        self.size += 1

    def _put(self, key, val, currentNode):  # recursive version
        # at current node, we insert a key-val, this pair will be placed in right pos
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                currentNode.leftChild.Successor = currentNode.leftChild.findSuccessor()
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                currentNode.rightChild.Successor = currentNode.rightChild.findSuccessor()
        elif key == currentNode.key:
            currentNode.payload = val

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:  # There are nodes in tree
            res = self._get(key, self.root)
            if res:  # this key is in tree
                return res.payload
            else:  # No this key in tree
                return None
        else:  # no node in tree
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key is not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key is not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # Leaf Nodes
            if currentNode == currentNode.parent.leftChild:  # Left Child
                currentNode.parent.leftChild = None
            else:  # Right Child
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # Middle position
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:  # Only one child node
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:  # root node
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # root node
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild is not None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        pass

    def rebalance(self, node):
        if self.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


def inorder(bstree):
    inorder_root(bstree.root)


def inorder_root(bstree_root):
    if bstree_root:
        inorder_root(bstree_root.leftChild)
        print(bstree_root.key)
        inorder_root(bstree_root.rightChild)


# Inorder using findSuccessor
def inorder_successor(bstree):
    current_node = bstree.root.findMin()
    while current_node:
        print(current_node.key)
        current_node = current_node.findSuccessor()


b = BinarySearchTree()
b.put(4, 10)
b.put(1, 18)
b.put(3, 89)
b.put(5, 9)

inorder(b)
inorder_successor(b)