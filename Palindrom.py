# not palindrom but pangram
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def check(text):
	return set(text.lower()).issuperset(set(alphabet))

print(check('abc'))
