import random
import time


# 1. Sequential search
def sequentialSearch(alist, item):
    i = 0
    Find = False
    while i < len(alist) and not Find:
        if alist[i] == item:
            Find = True
        else:
            i += 1
    return Find


sequentialSearch([2, 3, 45, 9], 4)


# 2. Ordered sequential search
def OrderedSequentialSearch(alist, item):
    i = 0
    Find = False
    smaller = (alist[i] <= item)
    while i < len(alist) and not Find and smaller:
        if alist[i] == item:
            Find = True
        elif alist[i] > item:
            smaller = False
        else:
            i = i + 1
    return Find


OrderedSequentialSearch([2, 3, 5, 6, 8, 91, 100], 10000)


# 3. Binary search (ordered list)
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while not found and first <= last:
        midpoint = (last + first) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return found


binarySearch([1, 2, 4, 5, 6, 8, 17, 19], 6)


# Generate random integers to compare the efficiency of 3 searches
def test_time(alist, item):
    start = time.time()
    sequentialSearch(alist, item)
    end = time.time()
    print('Sequential Search: {}'.format((end - start) * 100))
    # Sort the list
    random_list.sort()

    # Ordered sequential search
    start = time.time()
    OrderedSequentialSearch(alist, item)
    end = time.time()
    print('Ordered Sequential Search: {}'.format((end - start) * 100))

    # Binary search
    start = time.time()
    binarySearch(alist, item)
    end = time.time()
    print('Binary Search without ordering operation: {}'.format((end - start) * 100))


random.seed(1)
random_list = random.sample(range(10000000), k=1000000)
test_time(random_list, 9549656)

# test the time of two versions of binary search
random_list.sort()


def binarySearch_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            return binarySearch_recursive(alist[(midpoint + 1):], item)  # slice [1][1:] return []
        else:
            return binarySearch_recursive(alist[:midpoint], item)


binarySearch_recursive([1, 3, 5], 2)


# Recursive binary search without slicing operation
def binarySearch_recursive_modified(alist, item, first, last):
    if first > last:
        return False
    else:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            return binarySearch_recursive_modified(alist, item, midpoint + 1, last)
        else:
            return binarySearch_recursive_modified(alist, item, first, midpoint - 1)


def test_binary_search(random_list, item):
    start = time.time()
    binarySearch(random_list, item)
    end = time.time()
    print('Binary Search using loop: {}'.format((end - start) * 100))

    start = time.time()
    binarySearch_recursive(random_list, item)
    end = time.time()
    print('Binary Search using recursive: {}'.format((end - start) * 100))

    start = time.time()
    binarySearch_recursive_modified(random_list, item, 0, len(random_list) - 1)
    end = time.time()
    print('Binary Search using recursive without slicing: {}'.format((end - start) * 100))


test_binary_search(random_list, 9549656)


# 4. Hash searches
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # Store Keys
        self.data = [None] * self.size  # store values

    def put(self, key, data):
        hash_value = self.hashfunction(key, self.size)
        fill = False
        while not fill:
            if self.slots[hash_value] is None or self.slots[hash_value] == 'delete':
                # slot is none then insert key/value, change fill to end the loop. If delete field, is another way
                self.slots[hash_value] = key
                self.data[hash_value] = data
                fill = True
            elif self.slots[hash_value] == key:  # key has existed then update the data, change fill to end the loop
                self.data[hash_value] = data
                fill = True
            else:  # slot is not none and not existing key, then rehash
                hash_value = self.rehash(hash_value, self.size)

    def get(self, key):
        hash_value = self.hashfunction(key, self.size)
        start_pos = hash_value
        find = False
        stop = False
        while not find and not stop:
            if self.slots[hash_value] == key:
                find = True  # this key is in hash table and directly return the data in corresponding position
                result = self.data[hash_value]
            elif self.slots[hash_value] is None:
                stop = True  # this key is not in hash table
                result = None
            else:
                hash_value = self.rehash(hash_value, self.size)
                if hash_value == start_pos:  # Avoid the situation that all the slots are filled
                    # and loop until the first hash value
                    stop = True
                    result = None
        return result

    def hashfunction(self, key, size):
        return key % size  # return hash value

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size  # new hash value if slot is not none. % size to avoid 10 + 1 = 11 condition

    def __getitem__(self, key):  # want to use example[i] to represent get method
        return self.get(key)

    def __setitem__(self, key, value):  # want to use example[i] = value to represent put method
        self.put(key, value)

    def __len__(self):
        num = 0
        for i in range(self.size):
            if self.slots[i] is not None:
                num += 1
        return num

    def __contains__(self, item):
        return item in self.slots

    def __delitem__(self, key):  # 6 open addressing del method
        hash_value = self.hashfunction(key, self.size)
        start_pos = hash_value
        find = False
        stop = False
        while not find and not stop:
            if self.slots[hash_value] == key:
                self.slots[hash_value] = 'delete'
                self.data[hash_value] = 'delete'
                find = True
            elif self.slots[hash_value] is None:
                stop = True
            else:
                hash_value = self.rehash(hash_value, self.size)
                if hash_value == start_pos:
                    stop = True


hash_table = HashTable()
hash_table.put(1, 5)
hash_table.put(2, 4)
hash_table.slots
hash_table.data
hash_table.put(12, 6)
hash_table.slots
hash_table.data
hash_table.put(1, 9)
hash_table.slots
hash_table.data

hash_table[54] = 'cat'
hash_table[26] = 'dog'
hash_table[95] = 'lion'
hash_table.slots
hash_table.data


hash_table[54]
hash_table[54] = 'chicken'
hash_table[54]
print(hash_table[33])

len(hash_table)
12 in hash_table
3 in hash_table

del hash_table[12]
hash_table.slots
hash_table.data
hash_table.put(23, 'added thing')
hash_table.slots
hash_table.data


# Implement len() method for hash
def hash(astring, tablesize):
    Sum = 0
    for i in astring:
        order = ord(i)
        Sum += order
    return Sum % tablesize


hash('cat', 11)


def hash_modified(astring, tablesize):
    Sum = 0
    for i in range(len(astring)):
        order = ord(astring[i])
        weight = i + 1
        Sum += order * weight
    return Sum % tablesize


hash_modified('cat', 11)


# 6 Del method for linked list
# linked list
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, new_node):
        self.next = new_node

    def setData(self, new_data):
        self.data = new_data


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        current_node = self.head
        previous_node = None
        found = False

        while current_node is not None and not found:
            if current_node.getData() == item:
                if previous_node is None:
                    self.head = current_node.getNext()
                else:
                    previous_node.setNext(current_node.getNext())
                found = True
            else:
                previous_node = current_node
                current_node = current_node.getNext()

    def search(self, item):
        current = self.head
        find = False
        while current is not None and not find:
            if current.getData() == item:
                find = True
            else:
                current = current.getNext()
        return find


class HashTableLinkedList:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def put(self, key):
        hash_value = self.hashValue(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = LinkedList()
            self.slots[hash_value].add(key)
        else:
            self.slots[hash_value].add(key)

    def hashValue(self, key):
        return key % self.size

    def get(self, key):
        hash_value = self.hashValue(key)
        return self.slots[hash_value]

    def search(self, key):
        hash_value = self.hashValue(key)
        if self.slots[hash_value] is None:
            find = False
        else:
            find = self.slots[hash_value].search(key)
        return find

    def __delitem__(self, key):
        hash_value = self.hashValue(key)
        if self.slots[hash_value] is not None:
            self.slots[hash_value].remove(key)


a = HashTableLinkedList(11)
a.put(1)
a.put(2)
a.put(3)
a.put(12)
a.put(23)

a.search(2)
a.search(4)
a.get(1).head.getData()

del a[12]
a.get(1).head.getNext().getData()


# Open addressing expand capacity & quadratic probing
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # Store Keys
        self.data = [None] * self.size  # store values

    def put(self, key, data):
        hash_value = self.hashfunction(key, self.size)
        fill = False
        number = 1
        while not fill:
            if self.slots[hash_value] is None:  # slot is none then insert key/value, change fill to end the loop
                self.slots[hash_value] = key
                self.data[hash_value] = data
                fill = True
            elif self.slots[hash_value] == key:  # key has existed then update the data, change fill to end the loop
                self.data[hash_value] = data
                fill = True
            else:  # slot is not none and not existing key, then rehash
                hash_value = self.rehash(hash_value, self.size, number)
                number += 1

        if (len(self))/self.size > 0.999:  # when lambda larger than 0.9 expand the hash table
            self.size = 2 * self.size
            old_data = zip(self.slots, self.data)
            self.slots = [None] * self.size  # Store new Keys
            self.data = [None] * self.size  # Store new Keys
            for i, j in old_data:
                if i is not None and j is not None:
                    self.put(i, j)

    def get(self, key):
        hash_value = self.hashfunction(key, self.size)
        start_pos = hash_value
        find = False
        stop = False
        number = 1
        while not find and not stop:
            if self.slots[hash_value] == key:
                find = True  # this key is in hash table and directly return the data in corresponding position
                result = self.data[hash_value]
            elif self.slots[hash_value] is None:
                stop = True  # this key is not in hash table
                result = None
            else:
                hash_value = self.rehash(hash_value, self.size, number)
                number += 1
                if hash_value == start_pos:  # Avoid the situation that all the slots are filled
                    # and loop until the first hash value
                    stop = True
                    result = None
        return result

    @staticmethod
    def hashfunction(self, key, size):
        return key % size  # return hash value

    def rehash(self, oldhash, size, number):
        return (oldhash + number ** 2 - (number - 1) ** 2) % size

    def __getitem__(self, key):  # want to use example[i] to represent get method
        return self.get(key)

    def __setitem__(self, key, value):  # want to use example[i] = value to represent put method
        self.put(key, value)

    def __len__(self):
        num = 0
        for i in range(self.size):
            if self.slots[i] is not None:
                num += 1
        return num

    def __contains__(self, item):
        return item in self.slots


hash_table = HashTable()
hash_table.put(1, 5)
hash_table.put(2, 4)
hash_table.put(12, 6)
hash_table[54] = 'cat'
hash_table[26] = 'dog'
hash_table.slots
hash_table.data

hash_table[27] = 'lion'  # when lambda is 0.5, once this item is added, the table expands
hash_table.slots
hash_table.data

hash_quadratic_test = HashTable()
for i in [54, 26, 93, 17, 77, 31, 44, 55, 20]:
    hash_quadratic_test.put(i, 'same')

hash_quadratic_test.slots


# ##################################### Sort ###############################################

# 1. Bubble sort
def BubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


a = [2, 3, 1, 7, 9, 5]
BubbleSort(a)


# short bubble sort
def ShortBubbleSort(alist):
    stop = False
    passnum = len(alist) - 1
    while not stop and passnum > 0:
        stop = True
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                stop = False
        passnum -= 1


a = [2, 3, 1, 7, 9, 5]
ShortBubbleSort(a)


# Bidirectional bubble: Suitable for many small values at end sections of list
def bidirection_bubble(alist):
    start = 0
    end = len(alist) - 1
    while start < end:
        for i in range(start, end, 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        end -= 1
        if start < end:
            for j in range(end, start, -1):
                if alist[j] < alist[j - 1]:
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]
            start += 1


b = random.sample(range(50), 50)
bidirection_bubble(b)


# 2. Selection sort
def SelectionSort(alist):
    for passnum in range(len(alist), 0, -1):
        max_num = alist[0]
        max_index = 0
        for i in range(1, passnum):
            if alist[i] > max_num:
                max_num = alist[i]
                max_index = i
        alist[max_index], alist[passnum - 1] = alist[passnum - 1], alist[max_index]


a = [2, 3, 1, 7, 9, 5]
SelectionSort(a)


# 3. Insertion sort
def InsertionSort(alist):
    for i in range(1, len(alist)):
        insert_value = alist[i]
        location_insert = i
        while location_insert > 0 and alist[location_insert - 1] > insert_value:
            alist[location_insert] = alist[location_insert - 1]
            location_insert -= 1
        alist[location_insert] = insert_value


a = [2, 3, 1, 7, 9, 5]
InsertionSort(a)


# 4. Shell sort
def shellSort(alist):
    sublistcount = len(alist) // 2  # n/2 1st increment, n/4 second increment
    while sublistcount > 0:
        for startposition in range(0, sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        # print('After increments of size {}: the list is {}'.format(sublistcount, alist))
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """

    :param alist: A random list
    :param start: start value of sub list
    :param gap: increment
    :return: Sorted group
    """
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]  # If start = 0, gap = 2, then we start from insertion 3rd value in list
        position = i  # i = 2
        while position >= gap and current_value < alist[position - gap]:  # 3rd value smaller than last value then
            alist[position] = alist[position - gap]  # move last value to the current position
            position = position - gap  # move indicator to left to check whether value before is larger than current
        alist[position] = current_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

shellSort(alist)


# E13 shell sort
def shellSort(alist):
    sublistcount = len(alist) // 2  # n/2 1st increment, n/4 second increment
    while sublistcount > 0:
        for startposition in range(0, sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        # print('After increments of size {}: the list is {}'.format(sublistcount, alist))
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """

    :param alist: A random list
    :param start: start value of sub list
    :param gap: increment
    :return: Sorted group
    """
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]  # If start = 0, gap = 2, then we start from insertion 3rd value in list
        position = i  # i = 2
        while position >= gap and current_value < alist[position - gap]:  # 3rd value smaller than last value then
            alist[position] = alist[position - gap]  # move last value to the current position
            position = position - gap  # move indicator to left to check whether value before is larger than current
        alist[position] = current_value


def shellSort2(alist, increment):
    for startposition in range(0, increment):
        partition(alist, startposition, increment)
    InsertionSort(alist)


random.seed(1)
alist = random.sample(range(500), 500)
for i in range(1, 50):
    start = time.time()
    shellSort2(alist.copy(), i)
    end = time.time()
    print((end - start) * 1000)


# 5. Merge sort
def mergeSort(alist):
    # print('Splitting ', alist)
    if len(alist) > 1:
        mid = len(alist)//2
        alist_left = alist[:mid]
        alist_right = alist[mid:]

        mergeSort(alist_left)
        mergeSort(alist_right)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(alist_left) and j < len(alist_right):
            if alist_left[i] < alist_right[j]:
                alist[k] = alist_left[i]
                i = i + 1
            else:
                alist[k] = alist_right[j]
                j = j + 1
            k = k + 1

        while i < len(alist_left):
            alist[k] = alist_left[i]
            i = i + 1
            k = k + 1

        while j < len(alist_right):
            alist[k] = alist_right[j]
            j = j + 1
            k = k + 1

    # print('Merging', alist)


b = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(b)


# E14 merge not using slicing
def mergeSort(alist, start, end):
    """
    Merge sort
    :param alist: A list
    :param start: Start position, initial = 0
    :param end: End position, initial = len(alist) - 1
    :return: Sorted list
    """
    # print('Splitting ', alist)
    if start < end:
        mid = (start + end)//2

        mergeSort(alist, start, mid)
        mergeSort(alist, mid + 1, end)
        merge(alist, start, mid, end)

    # print('Merging', alist)


def merge(alist, start, mid, end):
    temp_list = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if alist[i] < alist[j]:
            temp_list.append(alist[i])
            i += 1
        else:
            temp_list.append(alist[j])
            j += 1

    while i <= mid:
        temp_list.append(alist[i])
        i += 1

    while j <= end:
        temp_list.append(alist[j])
        j += 1

    for k in range(len(temp_list)):
        alist[k + start] = temp_list[k]


a = [6, 9, 5, 10]
merge(a, 0, 1, 3)
mergeSort(a, 0, 3)

mergeSort(alist, 0, 499)


# 6. Quick sort
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivotvalue:
            left_mark += 1
        while left_mark <= right_mark and alist[right_mark] >= pivotvalue:
            right_mark -= 1
        if left_mark <= right_mark:  # if the condition of ending loop is wrong position of pivotavalue
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
        else:  # if the condition of ending loop is crossing of left mark and right mark
            done = True
    alist[right_mark], alist[first] = pivotvalue, alist[right_mark]
    return right_mark


b = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = [1, 2, 3, 4, 5]
partition(b, 0, len(b) - 1)
partition(a, 0, len(a) - 1)
quickSort(b)


# E15
def quickSortHelper(alist, first, last):
    if first < last:
        if last - first > 0:
            splitpoint = partition(alist, first, last)
            quickSortHelper(alist, first, splitpoint - 1)
            quickSortHelper(alist, splitpoint + 1, last)
        else:
            InsertionSort(alist)


# E16
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    first_value = alist[first]
    last_value = alist[last]
    mid = (first + last) // 2
    mid_value = alist[mid]
    if first_value < last_value:
        if first_value > mid_value:
            final_index = first
        elif last_value > mid_value:
            final_index = mid
        else:
            final_index = last
    elif mid_value > first_value:
        final_index = first
    elif mid_value < last_value:
        final_index = last
    else:
        final_index = mid

    alist[first], alist[final_index] = alist[final_index], alist[first]  # change the position of reference to first
    pivotvalue = alist[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivotvalue:
            left_mark += 1
        while left_mark <= right_mark and alist[right_mark] >= pivotvalue:
            right_mark -= 1
        if left_mark <= right_mark:  # if the condition of ending loop is wrong position of pivotavalue
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
        else:  # if the condition of ending loop is crossing of left mark and right mark
            done = True
    alist[right_mark], alist[first] = pivotvalue, alist[right_mark]
    return right_mark


a = [4, 9, 3, 10, 5, 15, 12, 24]
partition(a, 0, 7)
partition(a, 0, 3)
partition(a, 5, 7)

random.seed(1)
alist = random.sample(range(500), 500)
quickSort(alist)


# test time of different sort
def test_sort_time(num):
    random.seed(1)
    alist = random.sample(range(num), num)
    # Bubble sort
    start = time.time()
    ShortBubbleSort(alist.copy())
    end = time.time()
    print('Time for bubble sort is {}'.format((end - start)*1000))
    # Selection sort
    start = time.time()
    SelectionSort(alist.copy())
    end = time.time()
    print('Time for selection sort is {}'.format((end - start) * 1000))
    # Insertion sort
    start = time.time()
    InsertionSort(alist.copy())
    end = time.time()
    print('Time for Insertion sort is {}'.format((end - start) * 1000))
    # Shell sort
    start = time.time()
    shellSort(alist.copy())
    end = time.time()
    print('Time for shell sort is {}'.format((end - start) * 1000))
    # Merge sort
    start = time.time()
    mergeSort(alist.copy())
    end = time.time()
    print('Time for merge sort is {}'.format((end - start) * 1000))
    # Quick sort
    start = time.time()
    quickSort(alist.copy())
    end = time.time()
    print('Time for quick sort is {}'.format((end - start) * 1000))


test_sort_time(500)









