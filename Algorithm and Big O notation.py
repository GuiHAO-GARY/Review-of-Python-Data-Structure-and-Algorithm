from itertools import permutations


# 1. Anagram checking: Given two strings s1 and s2, judge whether they are a pair of anagram
# Here we assumes s1 and s2 have the same lengths, and no lower upper case issue

# Method 1: Traverse elements in s1, for each element find the same element in s2,
# once find it replace it with None in s2, otherwise they are not anagrams.
def anagramSolution1(s1, s2):
    s2_list = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        target = s1[pos1]
        pos2 = 0
        found = None
        while pos2 < len(s2_list) and not found:
            if target == s2_list[pos2]:
                s2_list[pos2] = None
                found = True
            else:
                pos2 += 1
        if found:
            pos1 += 1
        else:
            stillOK = False
    return stillOK


# Method 2: Sort strings first and then compare
def anagramSolution2(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()
    ind = 0
    match = True
    while ind < len(s1_list) and match:
        if s1_list[ind] == s2_list[ind]:
            ind += 1
        else:
            match = False
    return match


# Method 3: Brute force method, generate all possible permutation of s1, see whether s2 in it
def anagramSolution3(s1, s2):
    collections = [''.join(s) for s in permutations(s1)]
    return s2 in collections


# Method 4: Count number
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos1 = ord(s1[i]) - ord('a')
        c1[pos1] += 1
        pos2 = ord(s2[i]) - ord('a')
        c2[pos2] += 1
    j = 0
    match = True
    while j < 26 and match:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            match = False
    return match


def anagramSolution4_modified(s1, s2):
    # Not limited to a-z string
    s1_dict = {}
    s2_dict = {}
    for string in s1:
        if string in s1_dict.keys():
            s1_dict[string] += 1
        else:
            s1_dict[string] = 0

    for string in s2:
        if string in s2_dict.keys():
            s2_dict[string] += 1
        else:
            s2_dict[string] = 0
    match = True
    for k, v in s1_dict.items():
        if k in s2_dict.keys():
            if v != s2_dict[k]:
                match = False
                break
        else:
            match = False
            break
    return match


if __name__ == '__main__':
    print('Method 1: Search and eliminate\n')
    print("'python' and 'typhon' are anagrams? {}".format(anagramSolution1('python', 'typhon')))
    print("'python' and 'newpot' are anagrams? {}".format(anagramSolution1('python', 'newpot')))
    print('Time complexity of anagramSolution1: O(n^2)\n')
    print('**********************************************\n')
    print('Method 2: Sort \n')
    print("'python' and 'typhon' are anagrams? {}".format(anagramSolution2('python', 'typhon')))
    print("'python' and 'newpot' are anagrams? {}".format(anagramSolution2('python', 'newpot')))
    print('It seems like time complexity of 2nd method is O(n). However, the T(n) is determined by sort operation '
          'which is O(nlogn)')
    print('**********************************************\n')
    print('Method 3: Brute Force')
    print("'python' and 'typhon' are anagrams? {}".format(anagramSolution3('python', 'typhon')))
    print("'python' and 'newpot' are anagrams? {}".format(anagramSolution3('python', 'newpot')))
    print('Time Complexity: O(n!)')
    print('**********************************************\n')
    print('Method 4: Count Number')
    print("'python' and 'typhon' are anagrams? {}".format(anagramSolution4('python', 'typhon')))
    print("'python' and 'newpot' are anagrams? {}".format(anagramSolution4('python', 'newpot')))
    print('Time Complexity: O(n), however it sacrifices some spaces')
    print('Modified method 4, not limited to a - z')
    print("'python' and 'typhon' are anagrams? {}".format(anagramSolution4_modified('python', 'typhon')))
    print("'python' and 'newpot' are anagrams? {}".format(anagramSolution4_modified('python', 'newpot')))

