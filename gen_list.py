import os #

print(list(range(11)))

print([x*x for x in range(1,11) if x%2 == 0])

print([m+n for m in 'XYF' for n in 'QWE'])


print([d for d in os.listdir('.')])

