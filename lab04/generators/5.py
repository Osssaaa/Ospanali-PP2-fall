def Down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("n: "))
gen = Down(n)
for i in gen:
    print(i)