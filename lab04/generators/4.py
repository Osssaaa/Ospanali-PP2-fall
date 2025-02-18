def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

start = int(input("a: "))
end = int(input("b: "))
gen = squares(start, end)
for i in gen:
    print(i)