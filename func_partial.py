from functools import partial


int2 = partial(int, base = 2)


print(int2('11'))