from functools import reduce

def map_def(x):
    return x*x

gen = map(map_def,[1,2,3,4])
print(list(gen))

print(list(map(str,[1,2,3,4])))



def add(x,y):
    print(y)
    return x*2+y
print(reduce(add,[1,2,3]))