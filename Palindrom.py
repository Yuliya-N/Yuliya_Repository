# not palindrom but pangram
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def check(text):
	return(text.lower()).issuperset(set(alphabet))