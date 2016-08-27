a,b = 1,1
x = int(input("enter count:"))
while len(str(b))<x:
	a,b = b, a+b
print(b)