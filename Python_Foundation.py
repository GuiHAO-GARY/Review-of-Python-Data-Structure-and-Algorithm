import math

print('Hello, Algorithms and Data Structures')

# ------------- Data ---------------------------
# -------- Built-in data type ---------
# int, float
# Arithmetic Operators like +, -, *, / and **, %, //
7 ** 2  # 49
7 % 2  # mod: 1
7 // 2  # 3

# Bool value: Very useful in subsequent complex condition such as loop
# Boolean operators such as 'and', 'or', 'not'
True
False
True and False  # False
True or False  # True
not False  # True

# Logical Operators: <, >, <=, >=, ==, !=.
10 == 5  # False
10 > 5  # True
10 != 5  # True

# Assignment statement
# Note: A great variable name should refer to some actual meanings, which is easier for reading and understanding.

aNumber = 1
aString = 'a'

# ----------- Built-in Set Data Type ----------------
# List: A collection of elements which can be any data type, a sequential collection
myList = [1, 3, True, 6.5]

# Operation used to list
myList[0]  # Index, remember the first position starts from index 0
myList + ['new element']  # Concatenate
myList * 3  # Repeat myList 3 times and concatenate them together
1 in myList  # Whether element 1 is in myList
len(myList)  # Length of myList
myList[1:2]  # Slicing: extract a part of myList. Left of : is selected while right of : is not selected

# Method used to list
myList.append('add_item')  # Add element at the ending of list
myList.insert(0, 'insert_item')  # Insert at index 0
myList.pop()  # Delete the last element of list
myList.pop(2)  # Delete the index 2 element
myList.sort()  # Sort the element of list
myList.reverse()  # Rearrange the element in list with a reversed order
del myList[1]  # delete the item of mylist at index 1
myList.count(True)  # Count frequency of True in myList
myList.remove(6.5)  # Remove element 6.5 which appear firstly in myList

# List Comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

# range function generate a continuous sequence with start, end and step size
range(10)
range(0, 10)
list(range(10, 0, -1))
list(range(1, 5))

# String: Consists of alphabets, numbers and other symbols. A sequential collection
myName = 'Gary'
myName[2]
myName * 2
len(myName)

# Methods used to string
myName.center(1)
myName.count('a')  # 1
myName.ljust(1)
myName.rjust(1)
myName.lower()
myName.upper()
myName.find('r')  # 2
myName.split('a')  # ['G', 'ry']

# String is different from list respect with immutable property
# Tuple is also immutable
myTuple = (1, 2.9, True)
# myTuple[0] = 1 will generate error
# Tuple as records
lax_coordinates = (33.45645, 453.45645)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for country, _ in traveler_ids:
    print(country)

# Tuple unpacking
latitude, longitude = lax_coordinates
divmod(4, 8)
divmod(*(4, 8))  # * unpack the tuple
# Using * to grab excess items
a, b, *rest = range(5)
rest
a, *body, c, d = range(5)
body

# Slicing Object
a = list(range(5))
a[slice(1, 2)]  # equal to a[1:2]
a = ['string', 'apple', 'orange juice']
sorted(a)
sorted(a, key=len)
a = ['1', 3, 34, '45', '2']
sorted(a, key=int)

# Set: No sequence. No repeat value
mySet = {1, 1, 3, 4, 'cat', 5.5}
mySet
# Operation
1 in mySet
len(mySet)
otherSet = {2, 3, 'dog'}
mySet | otherSet  # Union, also can use mySet.union(otherSet)
mySet & otherSet  # Intersection, also can use mySet.intersection(otherSet)
mySet - otherSet  # Return elements only in mySet, also can use mySet.difference(otherSet)
mySet <= otherSet  # Whether elements in mySet are all in otherSet, also can use mySet.issubset(otherSet)

# Other methods used to set
mySet.add('new element')
mySet.pop()  # Randomly delete one element from set
mySet.clear()  # Clear all elements in set

# Dictionary: No sequence. A mapping from key to value.
# Generate dictionary
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict(b)

# dict comprehension
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
{code: country.upper() for country, code in country_code.items() if code < 66}

capitals = {'Iowa': 'DesMoines', 'Wisconsin': 'Madison'}

capitals['Iowa']  # Index
'Wisconsin' in capitals  # Whether key Wisconsin is in capitals dict
del capitals['Iowa']  # Delete assigned key-value pair

capitals.keys()  # dict_keys(['Iowa', 'Wisconsin'])
capitals.values()  # dict_values(['DesMoines', 'Madison'])
capitals.items()  # dict_items([('Iowa', 'DesMoines'), ('Wisconsin', 'Madison')])
capitals.get('Iowa')  # Similar with index
capitals.get('China', 'No this capital')  # Index to a non-existing return with an alternative


# Error Handling -------------------------------------------
# 1. Try except
def square_root(aNumber):
    try:
        print(math.sqrt(aNumber))
    except:
        print('Bad value for square root')
        print('Use absolute value instead')
        print(math.sqrt(abs(aNumber)))


square_root(1)
square_root(-1)


# 2. raise to cast error
def square_root(aNumber):
    if aNumber >= 0:
        print(math.sqrt(aNumber))
    else:
        raise RuntimeError('You cannot use a negative number!')


square_root(-1)