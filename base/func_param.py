def power(x = 1, n =2):
    s = 1
    for item in range(n):
        s*=x
    return s
print(power())



def add_end(L = []):
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())
print(add_end())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(calc([1,2,3,4]))
print(calc((1,2,3,4,5)))


