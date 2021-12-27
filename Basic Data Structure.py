import string
import random


# Stack: LIFO
# Use list to create stack
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # select the last element
        return self.items[-1]

    def size(self):
        return len(self.items)


# 1. One task to match bracket '(' ')' using Stack, only (, ) are in symbolString
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():  # Only when no condition ')' and '('.
        return True
    else:
        return False


# For different brackets () {} []
def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


def parChecker2(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        elif s.isEmpty():
            balance = False
        elif not matches(s.peek(), symbol):
            balance = False
        else:
            s.pop()
        index = index + 1

    if balance and s.isEmpty():
        return True
    else:
        return False


# 2. Transform decimal number into binary number
# Using the reversing property of stack
def divideBy2(decNumber):
    s = Stack()

    while decNumber != 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString


# Transform decimal number to base number
def divideByBase(decNumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while decNumber != 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base

    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    return binString


# 3. Medium order expression to Post ordered expression and calculation
def infixToPostfix(infixexpr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  # define priority of operator

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in string.ascii_uppercase:  # if the token is alphabet, add it directly into list
            postfixList.append(token)
        elif token == '(':  # if the token is (, push it into stack
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()  # once token is ), then remove top element of stack until the (, and remove (
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and prec[opStack.peek()] >= prec[token]:  # if token is + or -,
                # the final element in stack is * or / or + or -,
                # then can output final element
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ''.join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == '*':
        result = op1 * op2
    elif op == '/':
        result = op1/op2
    elif op == '+':
        result = op1 + op2
    else:
        result = op1 - op2
    return result


# Queue: First in First out FIFO
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# 1. Josephus problem
def hotPotato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)  # Enter the name in queue

    while q.size() > 1:
        i = 0
        while i < num:
            name_out = q.dequeue()
            q.enqueue(name_out)
            i = i + 1
        q.dequeue()  # End of queue is out

    return q.dequeue()


# 2. Simulation of a printer
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages

    def getStamp(self):
        return self.timestamp

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print('Average Wait %6.2f secs %3d tasks remaining.'%(averageWait, printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181) # one task per 180s
    if num == 180:
        return True
    else:
        return False


# Deque
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# 1. Palindrome Checker
def palChecker(astring):
    d = Deque()

    for string in astring:
        d.addFront(string)

    equalMark = True
    while d.size() > 1 and equalMark:
        front = d.removeFront()
        rear = d.removeRear()
        if front != rear:
            equalMark = False

    return equalMark


# Linked list
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __repr__(self):
        current = self
        string = ''
        while current:
            string += str(current.data) + '-->'
            current = current.next
        string = string + 'None'
        return string


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0

        while current is not None:
            current = current.getNext()
            count = count + 1

        return count

    def search(self, item):
        current = self.head
        found = False

        while (current is not None) and (not found):
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while (current is not None) and (not found):
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        current = self.head

        while current is not None:
            current = current.getNext()

        current.setNext(temp)

    def insert(self, loc, item):
        current = self.head
        previous = None
        temp = Node(item)
        temploc = 0

        while current is not None and temploc < loc:
            previous = current
            current = current.getNext()
            temploc = temploc + 1

        if previous is None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def index(self, item):
        current = self.head
        found = False
        index = 0

        while (current is not None) and (not found):
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1

        return index

    def pop(self, loc):
        current = self.head
        previous = None
        temploc = 0

        while current is not None and temploc < loc:
            previous = current
            current = current.getNext()
            temploc = temploc + 1
            value = current.getData()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return value


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while (current is not None) and (not found) and (not stop):
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        stop = False

        while current is not None and not stop:
            if current.getData() < item:
                previous = current
                current = current.getNext()
            else:
                stop = True

        if previous is None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


def ReverseList(head, left, right):
    """
    Reverse the linked list
    :param head: Head node of linked list
    :param left: Start position to reverse
    :param right: End position to reverse
    :return: New head with reversed linked list
    """
    if right - left < 0:
        print('Wrong input')
    elif right - left == 0:
        return head
    else:
        index = 1
        current = head
        if left == 1:
            node1 = None
            node2 = current
        else:
            while current and index < left - 1:
                current = current.next
                index += 1
            node1 = current
            index += 1
            node2 = current.next

        current = node2
        prev = None
        while current and index <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            index += 1
        if current:
            node2.next = current
        if node1:
            node1.next = prev
        else:
            head = prev
    return head


if __name__ == '__main__':
    s = Stack()
    print('Is stack s empty? {}'.format(s.isEmpty()))
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.pop())
    print(s.size())
    ####################################################
    hotPotato(['Sarah', 'David', 'John', 'Henry', 'Gary'], 3)
    ####################################################
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.setNext(b)
    b.setNext(c)
    c.setNext(d)
    d.setNext(e)

    ReverseList(a, 2, 4)

    c.setNext(e)
    ReverseList(c, 1, 2)

    ReverseList(a, 1, 1)





