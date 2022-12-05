import numpy as np

def groupElves(input,groups):
    i = 0
    g = 0   
    for lines in input:
        if i > 2:
            i = 0
            g = g + 1
        if i == 2:
            groups[g][2] = lines
        elif i == 1:
            groups[g][1] = lines
        elif i == 0:
            groups[g][0] = lines
        i = i + 1

def BadgePriority(group):
    for backpack in group:
        for itemType in backpack:
            if itemType in group[1] and itemType in group[2]:
                if itemType <= 'Z':
                    priority = ord(itemType) - ord('A') + 27
                else:
                    priority = ord(itemType) - ord('a') + 1 
                break
        break
    return priority

if __name__ == '__main__':
    input = open('input.txt').read().split('\n')
    groups = np.empty([(len(input) // 3),3], dtype = "object")
    groupElves(input,groups)

    sum = 0
    for group in groups:
        sum += BadgePriority(group)
    print(sum)