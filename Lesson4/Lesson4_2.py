def fact(n):
    if n == 1:
        return 1
    f = fact(n - 1)
    return f * n

print(fact(5))
