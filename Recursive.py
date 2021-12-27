from Basic_Data_Structure import Stack
from turtle import *
import time
import random
# Recursive
# Three points 1. Basic condition 2. Approaching to basic condition 3. Invoke self


# 1. Sum of list numbers
def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])


# 2. Transformation of decimal numbers
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return str(n)
    else:
        return toStr(n // base, base) + convertString[n % base]


def toStr(n, base):
    convertString = '0123456789ABCDEF'
    rstack = Stack()
    if n < base:
        rstack.push(convertString[n])
    else:
        rstack.push(convertString[n % base])
        toStr(n // base, base)


# 3. Use recursive way to draw pictures
def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)


# Draw a tree
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)


# Draw a triangle
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()


def getMid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)


# 4. Hannota problem: Move plate
def move(n, fromPole, toPole, withPole):
    if n >= 1:
        move(n - 1, fromPole, withPole, toPole)
        print(fromPole + '->' + toPole)
        move(n - 1, withPole, toPole, fromPole)


# 5. Minimum coin numbers given fixed total face value
# Recursive version
def recMC(coinValueList, change):
    """
    This function is to find optimal solution to give minimum coin numbers given total amount of change and coin face value
    :param coinValueList: List of coin value
    :param change: Total amount of change
    :return: the minimum coin number and the composition of combination
    """
    if change in coinValueList:
        return 1
    else:
        return min([(1 + recMC(coinValueList, change - x)) for x in coinValueList if x < change])


# print(recMC([1, 2, 3, 32, 50], 64))
# Use known results to decrease redundant calculations
def recMC(coinValueList, change, knownResults):
    """
    This function is to find optimal solution to give minimum coin numbers given total amount of change and coin face value
    :param coinValueList: List of coin value
    :param change: Total amount of change
    :param knownResults: Store known result， length equals to change. set to [0] * change
    :return: the minimum coin number and the composition of combination
    """
    if change in coinValueList:
        knownResults[change - 1] = 1
        return 1
    elif knownResults[change - 1]:
        return knownResults[change - 1]
    else:
        minCoin = min([(1 + recMC(coinValueList, change - x, knownResults)) for x in coinValueList if x < change])
        knownResults[change - 1] = minCoin
        return minCoin

# print(recMC([1, 2, 3, 32, 50], 64, [0] * 64))


# Dynamic prgramming
def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change + 1):

        if cents in coinValueList:
            minCoins[cents - 1] = 1

        else:
            temp_list = [minCoins[cents - x - 1] for x in coinValueList if cents - x > 0]
            minCoins[cents - 1] = min([x for x in temp_list if x != 0]) + 1
    return minCoins


# dpMakeChange([1, 5, 10, 21, 25], 63, minCoins=[0] * 63)
def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


# Recursive Exercise
# 1. calculate n factorial

def factorialCal(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    elif n < 0:
        print('n should not be negative')
    else:
        return n * factorialCal(n - 1)

# factorialCal(5)
# factorialCal(0)
# factorialCal(-1)


# 2. reverse list element
def reverseList(x):
    if len(x) == 1:
        return x
    elif len(x) == 2:
        x[0], x[1] = x[1], x[0]
        return x
    else:
        return x[(len(x) - 1):] + reverseList(x[1:(len(x) - 1)]) + x[:1]


# reverseList([1, 3, 4, 5, 7])
# reverseList([1, 3, 5, 7])

# or
def reverseList2(x):
    if len(x) == 1:
        return x
    else:
        # Here I use pop and insert. can also use slice
        last_element = x.pop()
        new_x = reverseList2(x)
        new_x.insert(0, last_element)
        return new_x


# reverseList2([1, 3, 4, 5, 7])


# double indicator
def reverseList3(x):
    i = 0
    j = len(x) - 1
    while i < j:
        x[i], x[j] = x[j], x[i]
        i += 1
        j -= 1
    return x


reverseList3([1, 3, 4, 5, 7])
reverseList3(list(range(10000)))  # This is more faster than recursive methods


# 3. modify the graph of recursive tree
# (1) modify the width of branch, the smaller branchLen is, the thinner the branch is
# (2) change color to emulate leaves
# (3) change angle randomly
# (4) change branchLen randomly
def tree(branchLen, t):
    if branchLen > 5:
        t.pensize(width=branchLen/10)
        t.color('black')
        if branchLen < 6:
            t.color('green')
        t.forward(branchLen)
        angle_change = random.uniform(20, 35)
        t.right(angle_change)
        tree(branchLen - random.uniform(0, branchLen/1.3), t)
        t.left(angle_change * 2)
        tree(branchLen - random.uniform(0, branchLen/1.3), t)
        t.right(angle_change)
        t.backward(branchLen)


# t = Turtle()
# myWin = t.getscreen()
# t.left(90)
# t.up()
# t.backward(300)
# t.down()
# tree(110, t)
# myWin.exitonclick()

# 5 Febonacci array list
def febonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return febonacci_recursive(n - 1) + febonacci_recursive(n - 2)

# febonacci_recursive(6)


# use iteration
def febonacci_loop(n):
    x = [0] * (n + 1)
    x[1] = 1
    i = 0
    while i <= (n - 2):
        x[i + 2] = x[i] + x[i + 1]
        i = i + 1
    return x


# febonacci_loop(15)


# compare the performance of two algorithm
# t1 = time.time()
# a = febonacci_recursive(30)
# t2 = time.time()
# print('Recursive will spend {}s'.format(t2 - t1))
#
# t1 = time.time()
# b = febonacci_loop(30)
# t2 = time.time()
# print('Loop will spend {}s'.format(t2 - t1))


# It seems recursive takes too much time on unnecessary calculation
# modify the recursive function
def febonacci_recursive2(n, known_value):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif known_value[n]:  # check whether this value is 0, if not zero directly return this value
        return known_value[n]
    else:  # this means the febonacci(n) has not been calculated
        known_value[n] = febonacci_recursive2(n - 1, known_value) + febonacci_recursive2(n - 2, known_value)
        return known_value[n]

# t1 = time.time()
# a = febonacci_recursive(30)
# t2 = time.time()
# print('Recursive will spend {}s'.format(t2 - t1))
#
# t1 = time.time()
# a = febonacci_recursive2(30, [0]*31)
# t2 = time.time()
# print('Modified recursive will spend {}s'.format(t2 - t1))


# 6 Hannota

state = {'A': ['Big', 'Middle', 'Small'],
         'B': [],
         'C': []}


def move(n, fromPole, toPole, withPole):
    if n >= 1:
        move(n - 1, fromPole, withPole, toPole)
        print(fromPole + '->' + toPole)
        plate = state[fromPole].pop()
        state[toPole].append(plate)
        print(state)
        move(n - 1, withPole, toPole, fromPole)


# move(3, 'A', 'B', 'C')


# 9. 10. Two bottle. The container sizes are a and b gallons but no tick marks.
# How to fill c gallons water into container with a gallons? You can only fill up containers.
def operate(sizeA, sizeB, requiredC):
    """
    A,B containers with size A, B. Assume sizeA > sizeB, requiredC. Want to fill requiredC gallons in A container
    :param sizeA:
    :param sizeB:
    :param requiredC:
    :return: Operation
    """

    if requiredC % sizeB == 0:
        if requiredC > sizeA:
            print('Full B and transform water from B to A for {} times '
                  'and then Full B again to fill A until A is full'.format(requiredC // sizeB - 1))
        else:
            print('Full B and transform water from B to A for {} times'.format(requiredC // sizeB))
    elif sizeA % sizeB == 0:
        print('It is impossible to do this task')
    elif requiredC > sizeB:
        operate(sizeA, sizeB, requiredC % sizeB)
        if requiredC > sizeA:
            print('Full B and transform water from B to A for {} times '
                  'and then Full B again to fill A until A is full'.format(requiredC // sizeB - 1))
        else:
            print('Full B and transform water from B to A for {} times'.format(requiredC // sizeB))
    else:
        operate(sizeA, sizeB, sizeA + requiredC)
        print('Remove water in A and transform remained water {} gallons in B to A  '
              'Now A has {} gallons water'.format(requiredC, requiredC))


# operate(10, 3, 7)
# operate(13, 5, 8)
# operate(12, 4, 6)
# operate(12, 3, 6)

# logical chain. Think reversely
# (10, 3, 7) -> (10, 3, 1) + 2 times pour -> (10, 3, 10 + 1) + remove A water + 2 times pour ->
# (10, 3, 2) + 3 times pour + ...


# 13. Paska triangle
def paska(row):
    if row == 1:
        return [1]
    elif row == 2:
        return [1, 1]
    else:
        temp_list = paska(row - 1)
        sum_list = []
        for i in range(len(temp_list) - 1):
            sum_list.append(temp_list[i] + temp_list[i + 1])
        return [1] + sum_list + [1]

# paska(50)


# 14 dynamic programming1
def getArt(ws, weightList, valueList, maxValue, solution):
    total_value = 0
    newArt = None
    for w in range(ws + 1):
        for j in [c for c in weightList if c <= w]:
            value = valueList[weightList.index(j)]
            if maxValue[w - j] + value > total_value:
                total_value = maxValue[w - j] + value
                newArt = j
        maxValue[w] = total_value
        solution[w] = newArt
    return maxValue, solution


def solution_output(ws, solution, maxValue):
    result = []
    total_value = maxValue[ws]
    while ws > 1:
        result.append(solution[ws])
        ws = ws - solution[ws]
    final_solution = {'solution': result,
                      'total value': total_value}
    return final_solution


maxValue, solution = getArt(20, [2, 3, 4, 5, 9], [3, 4, 6, 8, 10], maxValue=[0]*21, solution=[0]*21)
solution_output(19, solution, maxValue)

if __name__ == '__main__':
    print('1. Sum of list numbers [1, 2, 3]: {}'.format(listSum([1, 2, 3])))
    ########################################################################
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()
    ########################################################################
    t = Turtle()
    myWin = t.getscreen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color('green')
    tree(110, t)
    myWin.exitonclick()
    #########################################################################
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()
    myPoints = [(-500, -250), (0, 500), (500, -250)]
    sierpinski(myPoints, 5, myTurtle)
    myWin.exitclick()
    #########################################################################
    cl = [1, 5, 10, 21, 25]
    coinsUsed = [0] * 64
    coinCount = [0] * 64
    dpMakeChange(cl, 63, coinCount, coinsUsed)
    printCoins(coinsUsed, 63)