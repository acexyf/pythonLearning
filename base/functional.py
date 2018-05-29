from functools import reduce

def double(x):
    return x*x

print(list(map(double, [1,2,3,4])))

print('')

def fn(x,y):
    return str(x)+str(y)

print(reduce(fn, [1,2,3,4]))

print('')

def is_odd(n):
    return n%2==1

print(list(filter(is_odd, [1,2,3,4,5,6,7,9])))


