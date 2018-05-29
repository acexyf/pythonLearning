import os


arr = list(filter(lambda x: x.find('.py')!=-1, os.listdir('./')))

print(len(arr))