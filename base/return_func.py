def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


fn1 = lazy_sum(1,2,3,4,5)
print(fn1())

print('')


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())

print('')

def count1():

    def f(j):
        def g():
            return j*j
        return g  
    fs.append(f(i))
    fs = []
    for i in range(1,4):
    return fs

f4, f5, f6 = count1()

print(f4(), f5(), f6())







