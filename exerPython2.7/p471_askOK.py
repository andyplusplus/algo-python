
def ask_ok(prompt, retries=4, complaint='yes or no, please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no'):
			return False
		retries -= 1
		if retries < 0:
			raise IOError('refuse nik user')
		print complaint

ask_ok("how are you:")
