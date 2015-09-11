def fib(n):
	a,b = 0, 1
	while a<n:
		print a
		a,b = b, a+b

fib(2000)

def fib2(n):
	result = []
	a,b = 0, 1
	while a<n:
		result.append(a)
		a,b = b, a+b
	return result

fib100 = fib2(100)

print fib100

def fib3(n):
	r = []
	a,b = 0, 1
	while a<n:
		r.append(a)
		a,b = b, a+b
	return r

print fib3(100)


def ask_ok(prompt, retries=4, complaint='yes or no, please!'):
	while True:
		ok = 'yes' #raw_input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nope'):
			return False
		retries -= 1
		if retries < 0:
			raise IOError('refusenik user')
		print complaint

def ask_ok2(prompt, retries = 4, complaint = 'yes or no, please!'):
	while True:
		ok = 'yes' #raw_input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries -= 1
		if retries < 0:
			raise IOError('refusenik user')
		print complaint

def cheeseshop(kind, *arguments, **keywords):
	print "-- Do you have any", kind, "?"
	print "-- I'm sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print "-" * 40
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def write_multiple_items(file, sepataror, *args):
	file.write(sepataror.join(args))

args = [3,6]
range(*args)

def parrot(voltage, state='a stiff', action='voom'):
	print "-- This parrot wouldn't", action,
	print "if you put", voltage, "volts through it.",
	print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

def make_incrementor(n):
	return lambda x:x+n

f = make_incrementor(42)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair:pair[1])