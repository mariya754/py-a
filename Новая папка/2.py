n=100
print(2 ** 2)
for i in range (3, n+1):
    k=2
    while i%k != 0:
        k += 1
    if k == i:
        print(i**2)