import os
classMates = ['a','b','c','d']
classMates.append('last')
classMates.append('last one')
classMates.insert(1,'No1')
classMates.pop(3)
print(classMates)
print(len(classMates))

print(list(range(1,6)))

print('')

print([x*x for x in range(1,11) if x%2==0 ])

print(range(1,4))

print([m+n for m in 'ABC' for n in 'abc'])


print([d for d in os.listdir('.')])

list = ['QW','AS','ZX']

print([d.lower() for d in list])

print([d for d in range(1,4)])