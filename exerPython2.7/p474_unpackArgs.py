

###############################################
#  4.74 Unpacking Argument Lists
###############################################
print range(3,6)
args = [3,6]

range(*args)


def parrot(voltage, state='a stiff', action='voom'):
    print "voltate=", voltage
    print "action=", action
    print "state=", state

d = {"voltage" : "4000", "state" : "ssss", "action" : "voom"}

parrot(**d)


###############################################
#  4.75 Lambda Expressions
###############################################

def make_increment(n):
    return lambda x: x+n

f = make_increment(42)

print f(0)
print f(1)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

print pairs

#5.1.2. Using Lists as Queues
from collections import deque
queue = deque(["a", "b", "c"])
queue.append("Terry")
queue.append("gr")
print queue.popleft()

#5.1.3. Functional Programming Tools
def f(x): return x%3==0 or x%5==0
print filter(f, range(2,25))

def cube(x): return x*x*x
print map(cube, range(1, 22))

#5.1.4. List Comprehensions
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]