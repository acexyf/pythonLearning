from collections import Iterable

dist = {
    'Michael':95,
    'Bob':13,
    'Tracy':36
}
for key in dist:
    print(key, dist[key])

print('')


for ch in 'ASDFG':
    print(ch);

print('')

print(isinstance([],Iterable))
print(isinstance(123,Iterable))
print(isinstance('123',Iterable))
print(isinstance(dist,Iterable))

print('')


arr = ['a','b','c','d']

for index,value in enumerate(arr):
    print(index, value)
