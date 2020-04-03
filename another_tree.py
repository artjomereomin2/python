n1 = int(input())
n = 3
n2 = n1 - 1
for f in range(1, n1 + 1):
    for q in range(1, 2 + f):
        print(" " * (n - q - 1 + n2) + "*" * ((q - 1) * 2 + 1))
    n += 1
    n2 -= 1