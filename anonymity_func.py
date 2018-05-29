print(list(map(lambda x:x*x, [1,2,3,4,5,6,7])))

print('')

fn = lambda x: x*x
print(fn(2))

print('')

def build(x,y):
    return lambda: x*x+y*y

fn1 = build(1,4)

print(fn1())
