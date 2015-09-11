from collections import deque
queue=deque([])
queue.append('hello')

def f(x): return x%3 ==0 or x%5==0
filter(f, range(2,25))

def cube(x): return x*x*x
map(cube, range(1,11))

seq = range(8)
def add(x,y): return x+7
map(add, seq, seq)

def add(x, y): return x+y
reduce(add, range(1, 11))

def sum(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 0)

sum(range(1,11))

list1 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
list2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

freshfruit1 = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit2 = [w.strip() for w in freshfruit1]

z = [(x, x**2) for x in range(6)]

matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix2 = [[row[i] for row in matrix1] for i in range(4)]
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

for i in reversed(xrange(1,10,2)):
    print i

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
    print f

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.iteritems():
    print k, v
