import numpy as np

input = open('example.txt').read().split('\n')
length = len(input) // 3
groups = np.empty([length,3], dtype = "object")

sum = 0

i = 0
g = 0

for data in input:
    if i == 2:
        groups[g][2] = data
        g = g + 1
        i = 0
        print("New Group")
    elif i == 1:
        groups[g][1] = data   
    elif i == 0:
        groups[g][0] = data

    i = i + 1

print(groups)