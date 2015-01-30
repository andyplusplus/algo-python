__author__ = 'andy'

'''
753: 7*00 + 5*0 + 3
equal:
    all num_1     0 <= 700
           _2   701 <= 750
           _3   751 <= 753
    for _1:
    7     0    0    +1
    0-6  0-9  0-9

    for _2:
          5    0    +1 -1: +1 include 50, -1 for exclude 0
         0-4   0-9
    for _3:
               3
               1-3
'''

#iter 0 to n, count all number with out 4
def bruteforceM(n):
    sum = 0
    for i in range(1, n+1):
        nstr = str(i)
        if(nstr.find('4')==-1):
            sum += 1
    return sum

'''
700  hiDig = 7, tens = 2:  return (7-1)*9**2    #-1 to exclude 4
 50          5         1          (5-1)*9**1
  3          3         0
'''
def countTensM(hiDig, tens):
    sum = 0
    #if hiDig==4 and tens>0: sum = -1

    if hiDig>=4 and tens==0:
        hiDig -=1
    elif hiDig>=5 and tens>0:
        hiDig -= 1

    if tens<0:
        return 0
    else:
        sum += hiDig * 9**tens
        return hiDig * 9**tens

#return hiDig, digits
def countDigitsM(n):
    sum = 0; nTens=-1
    while n>0:
        nTens +=1; nDig = n%10
        if(nDig == 4): sum = -1
        sum += countTensM(nDig, nTens)
        n = n//10
    return sum

def main():
    a = [5426, 4426, 3, 7, 0, 13, 80, 31, 51, 751, 426]
    for i in a:
        print(i, " : \t", end="")
        print(bruteforceM(i), "\t", end="")
        print(countDigitsM(i))

main()