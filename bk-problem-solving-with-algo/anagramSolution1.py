__author__ = 'a'

"""Check whether two words is anagram"""

def anagramSolution_usingSet(s1, s2):
    if len(s1) != len(s2): return False
    l1 = list(s1); l2 = list(s2)

    s = {}
    for c in l1:
        if c in s:
            s[c] += 1
        else:
            s[c] = 1
    for c in l2:
        if c in s and s[c]>0:
            s[c] -= 1
        else:
            return False
    return True

def anagramSolution_useSort(s1, s2):
    if len(s1) != len(s2): return False
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    for i in range(len(s1)):
        if(l1[i] != l2[i]):
            return False
    return True

methods = [anagramSolution_usingSet, anagramSolution_useSort]

for method in methods:
    print(method)
    print(method("abcd", "bcda"))
    print(method("abcd", "bcdd"))