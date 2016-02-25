import re

re.findall(r'\bf[a-z]*', 'which root or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')

import random
random.choice(['apple', 'pear', 'banana'])

random.sample(xrange(100), 10)
random.random()

random.randrange(6)