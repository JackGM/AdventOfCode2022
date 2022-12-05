import numpy as np

input = open('input.txt').read().split('\n')
length = len(input) // 3
groups = np.empty([length,3], dtype = "object")
#print(groups)

sum = 0
i = 0
g = 0

for lines in input:
    if i > 2:
        i = 0
        g = g + 1
        #print("next group")

    #print(lines)

    if i == 2:
        groups[g][2] = lines
        #print("i=2")
    elif i == 1:
        groups[g][1] = lines
        #print("i=1")
    elif i == 0:
        groups[g][0] = lines
        #print("i=0")

    i = i + 1

#print(groups)
#print("-----")
i = 0

for group in groups:
    #print(group)
    for backpack in group:
        #print(backpack)
        for itemType in backpack:
            if itemType in group[1] and itemType in group[2]:
                if itemType <= 'Z':
                    priority = ord(itemType) - ord('A') + 27  # Index Upper Case from 1
                else:
                    priority = ord(itemType) - ord('a') + 1 # Index Lower Case from 1
                print(itemType)
                print(priority)
                break
        break
    print("add to total")
    sum += priority
print(sum)