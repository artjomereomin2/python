n = int(input())
for f in range(1, n + 1):
    print(" " * (n - f) + "*" * ((f - 1) * 2 + 1))