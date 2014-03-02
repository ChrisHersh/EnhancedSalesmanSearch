import math
import itertools

array = [1,2,3,4,5,6,7,8,9,10]
key = 4

def generateSubsets(lst, n):
    return [lst [t:t+n] for t in range ( 0, len(lst) + 1 - n)]
    
subsets = []
for i in range(1, len(array)+1):
    subsets.append(generateSubsets(array, i))
#print(subsets)
permutes = []
for x in range(0, len(subsets)):
    for i in range(0, len(subsets[x])):
        tmpPermutes = list(itertools.permutations(subsets[x][i]))
        for y in range(0, len(tmpPermutes)):
            permutes.append(tmpPermutes[y])
keyFound = False
for i in range(0, len(permutes)):
    if(len(permutes[i]) == 1):
        if(permutes[i][0] == key):
           keyFound = True
#print(permutes)
if(keyFound):
    print("Key Found")
else:
    print("Key not found")