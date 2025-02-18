def Even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
gen = Even(n)
for i in range(n // 2 + 1):
    print(next(gen), end=", " if i != (n // 2) else "")