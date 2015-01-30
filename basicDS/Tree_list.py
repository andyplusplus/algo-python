__author__ = 'andy'

my_tree = ['a', ['b',
                 ['d',[],[]], ['e',[],[]] ],
           ['c', ['f',[],[]], []] ]
print(my_tree)

print('left =', my_tree[1])
print('root =', my_tree[0])
print('righ =', my_tree[2])

print(">>>>>>>>>>>> tree <<<<<<<<<<\n")

def binary_tree(r):
    return [r, [], []]
