def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 1)


for i in range(6):
    print(f(i))
