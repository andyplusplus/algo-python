#=======================================================
# 5.1.0 More on lists
#=======================================================
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.23), a.count('x')

a.insert(2, -1)
a.append(333)

print a

a.index(333)
a.remove(333)
a.reverse()
a.sort()
a.pop()
print a
#=======================================================
# 5.1.1 Using lists as stacks
#=======================================================
stack = [3,4,5]
stack.append(7)
stack.append(8)
stack.append(9)
stack.pop()
stack.pop()
print stack

#=======================================================
# 5.1.2 Using Lists as Queues
#=======================================================
from collections import deque
queue = deque(["a", "b", "c"])
queue.append("d")
queue.append("e")
queue.popleft()
queue.popleft()
print queue

#=======================================================
# 5.1.3 Functional Programming Tools
#=======================================================

def f(x): return x%3 == 0 or x%5 == 0
print filter(f, range(2,25))

def cube(x): return x*x*x
print map(cube, range(1,22))

seq = range(8)
def add(x, y): return x+y
print map(add, seq, seq)
print reduce(add, range(1,11))

def sum(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 0)

print sum(range(1,11))
#=======================================================
# 5.1.4 List Comprehensions
#=======================================================
squares = []
for x in range(10):
    squares.append(x**2)

squares2 = [x**2 for x in range(10)]
print squares
print squares2

print [(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y]

vec = [-1, -2, 0, 2, 4]
y = [x*2 for x in vec]
z = [x for x in vec if x>=0]
v = [abs(x) for x in vec]
fresh_fruit = [' banana ', ' loganberry ', 'passion fruit ']
a = [weapon.strip() for weapon in fresh_fruit]
b = [(x, x**2) for x in range(6)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
c = [num for elem in vec for num in elem]

#=======================================================
# 5.1.4 Nested List Comprehensions
#=======================================================
matrix = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
d = [[row[i] for row in matrix] for i in range(4)]

transpond = []
for i in range(4):
    transpond.append([row[i] for row in matrix])

#=======================================================
# 5.3 Tuples and Sequences
#=======================================================
t = 12345, 54321, 'hello!'
u = t, (1,2,3,4,5)
x = ([1,2,3], [3,2,1])
empty = ()
singleton = 'hello',
print len(empty)
print len(singleton)
x1, y1, z1 = t


#=======================================================
# 5.4 Sets & Dictionary
#=======================================================
basket = ['a', 'b', 'c', 'd', 'e']
fruit = set(basket)
print fruit
print 'a' in fruit

tel = {"jack": 4098, 'sape': 4139}
tel['guid'] = 4127
del tel['jack']
print 'jack' in tel



#=======================================================
# 5.1.3 Functional Programming Tools
#=======================================================
#=======================================================
# 5.1.3 Functional Programming Tools
#=======================================================
