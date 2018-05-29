gen = (x*x for x in range(10))


# for item in gen:
#     print(item)



print(next(gen))
print(next(gen))


print('')

for n in gen:
    print(n)



print('')




def add(x, y, f):
    print(x)
    return f(x) + f(y)


x=7
print(x)


print('')

print(add(-2,-4,abs))