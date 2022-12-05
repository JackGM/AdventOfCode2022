import numpy as np

def groupElves(input,groups):  
    for g,lines in enumerate(input):
        sections = lines.split(',')
        groups[g][0] = sections[0].split('-')[0]
        groups[g][1] = sections[0].split('-')[1] 
        groups[g][2] = sections[1].split('-')[0]
        groups[g][3] = sections[1].split('-')[1]

def findEnclosedPairs(group):
    lowerPair = group[0] - group[2]
    upperPair = group[1] - group[3]

    if abs(lowerPair) + abs(upperPair) != abs(lowerPair + upperPair) or lowerPair == 0 or upperPair == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = open('input.txt').read().split('\n')
    groups = np.empty([len(input),4], dtype = "int")
    groupElves(input,groups)

    sum = 0
    for group in groups:
        sum += findEnclosedPairs(group)
    print(sum)