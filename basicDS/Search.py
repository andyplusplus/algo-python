__author__ = 'andy'

test_list = [3, 1, 2, 7, 0, 9, 4, 6, 5, 8]

def seq_s(list, item):
    pos = 0
    found = False
    while pos<len(list) and not found:
        if(list[pos] == item):
            found = True
        else:
            pos += 1
    return found

#print(seq_s(test_list, 7))

def ord_seq_s(list, item):
    pos = 0
    found = False
    while pos<len(list) and list[pos]<=item and not found:
        if list[pos] == item:
            found = True
        else:
            pos += 1
    return found

test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#print(ord_seq_s(test_list2, 3))
#print(ord_seq_s(test_list2, 8))
#print(seq_s(test_list, 7))

def binary_s(list, item, lo=None, hi=None):
    if lo == None:
        lo = 0
    if hi == None:
        hi = len(list) - 1
    if(lo>hi):
        return -1

    while(lo<=hi):
        m = (lo+hi)//2
        if(list[m] == item):
            return m
        elif list[m] < item:
            return binary_s(list, item, m+1, hi)
        else:
            return binary_s(list, item, lo, m-1)

print(binary_s(test_list2, 8))
print(binary_s(test_list2, 9))