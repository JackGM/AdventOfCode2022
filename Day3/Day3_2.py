import numpy as np

input = open('example.txt').read().split('\n')
length = len(input)
# groups = [['0'] * 3] * 300
groups = np.empty([5,5], dtype = "object")
print(groups)

# for g in groups:
#     print(g)
# print('#'*50)

sum = 0

i = 0
g = 0

for data in input:
    # print(groups)
    if i > 2:
        i = 0

    if i == 2:
        groups[g][2] = data
        g = g + 1
    elif i == 1:
        groups[g][1] = data   
    elif i == 0:
        groups[g][0] = data

    i = i + 1

    print(groups)