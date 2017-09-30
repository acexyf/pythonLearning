dist = {
    'Michael':95,
    'Bob':13,
    'Tracy':36
}

print('asd' in dist)

print('')

for item in dist:
    print(item)

print('')

print(dist.get('Bob'))
print(dist.get('Bobs'))
print(dist.get('Bobs', -1))


dist.pop('Tracy')
print(dist)