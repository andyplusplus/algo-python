class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self):
        self.data = []
    def f(self):
        return 'hello world'

x = MyClass()

print x.f()


class Complex:
    def __init__(self, realp, imagp):
        self.r = realp
        self.i = imagp

y = Complex(3.0, 4.0)

xf = x.f()

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print d.kind, "  ", e.name

class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
d.add_trick("trick 1")
d.add_trick("trick 2")
print d.tricks

#=======================================================
# d.add_trick("trick 1")
#=======================================================

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'


class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self,x):
        self.data(x*2)

bag = Bag()
print bag.__class__


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

class Employee:
    pass
john = Employee()
john.name = 'john doe'
john.dept = 'computer lab'
john.salary = 1000

'''
raise Class, inst
raise instance
raise instance.__class__, instance
'''
class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"

print "Iterators"
for element in [1,2,3]:
    print element
for element in (1,2,3):
    print element

for element in (1,2,3):
    print element
for element in (1,2,3):
    print element
for key in {'one':1, 'two':2}:
    print key
for char in "123":
    print char
#for line in open ("myfile.txt"):
#    print line

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
#for ch in rev:
#    print ch

def reverse(data):
    for index in range(len(data) -1, -1, -1):
        yield data[index]

for ch in reverse('golf'):
    print ch

sum(i*i for i in range(10))
xvec = [10, 20, 30]
yvec = [7, 5, 3]

print sum(x*y for x,y in zip(xvec, yvec))


from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91))
#unique_words = set(word for line in page for word in line.split())
#valedictorian = max((student.gpa, student.name) for student graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
#=======================================================
#
#=======================================================
