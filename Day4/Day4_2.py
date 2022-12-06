import numpy as np

def groupElves(input,groups):  
    for g,lines in enumerate(input):
        sections = lines.split(',')
        groups[g][0] = sections[0].split('-')[0]
        groups[g][1] = sections[0].split('-')[1] 
        groups[g][2] = sections[1].split('-')[0]
        groups[g][3] = sections[1].split('-')[1]

def findOverlappingPairs(group):
    match = 0
    for assignment in range(group[0],(group[1] + 1)):
        if assignment in range(group[2],(group[3] + 1)):
            match = match + 1
    if match > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = open('input.txt').read().split('\n')
    groups = np.empty([len(input),4], dtype = "int")
    groupElves(input,groups)

    sum = 0
    for group in groups:
        sum += findOverlappingPairs(group)
    print("Sum - ",sum)