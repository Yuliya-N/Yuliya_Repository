a, b = 1, 1
while b <= 10**999:
    a,b = b, a + b
print(b)