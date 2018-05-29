# 1*1+2*2+3*3+4*4+....
def calcs(*numbers):
    sums = 0
    for n in numbers:
        sums = sums+n*n
    return sums

mylist = [1,2,3,4,5]

print(calcs(*mylist))


# print(calcs(1,2,3,4))