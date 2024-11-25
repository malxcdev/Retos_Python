a = 0
b = 1

print(a)
print(b)
for _ in range(0, 50):
    a,b = b, a+b
    print(b)