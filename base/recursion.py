def recur(num, prod):
    if(num == 1):
        return prod
    return recur(num - 1, num*prod)

print(recur(5, 1))
