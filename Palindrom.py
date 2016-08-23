# not palindrom but pangram
from string import ascii_lowercase as az


def check(text):
	return set(text.lower()).issuperset(set(az))

print(check('abc') == False)
print(check('abcdefghijklmnopqrstuvwxyz'))
print(check('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
print(check('Quick brown fox jumps over the lazy dog'))