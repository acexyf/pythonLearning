gen = (x*x for x in range(10))


# for item in gen:
#     print(item)


def add(x, y, f):
    print(x)
    return f(x) + f(y)


x=7
print(x)

print(add(-2,-4,abs))