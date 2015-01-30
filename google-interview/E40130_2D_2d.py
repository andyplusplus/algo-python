__author__ = 'andy'

def gen(a, pre,i):
    if i == 3:
        print(pre, end=" ")
        return
    for str in a[i]:
        gen(a, pre+str, i+1)

def main():
    a = [["abc", "def", "gh"], ["f", "g"], ["qrt","xyz", "pqr"]]
    gen(a, "", 0)


main()