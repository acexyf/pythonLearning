from collections import Iterable

dist = {
    'Michael':95,
    'Bob':13,
    'Tracy':36
}

for ch in 'ASDFG':
    print(ch);

print(isinstance([],Iterable))
print(isinstance(123,Iterable))
print(isinstance('123',Iterable))
print(isinstance(dist,Iterable))
