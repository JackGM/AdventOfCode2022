import numpy as np

if __name__ == '__main__':
    input = open('input.txt').read().split('\n')
    rows = len(input)
    columns = len(input[0])
    tree_height = np.zeros([rows,columns], dtype = "object")

    LRSearch = np.zeros([rows,columns], dtype = "object")
    RLSearch = np.zeros([rows,columns], dtype = "object")
    TBSearch = np.zeros([columns,rows], dtype = "object")
    BTSearch = np.zeros([columns,rows], dtype = "object")
    Search = np.zeros([columns,rows], dtype = "object")

    for row_index,line in enumerate(input):
        for column_index,height in enumerate(line):
            tree_height[row_index][column_index] = height

    for y in range(1,rows-1):

        heightMax_LR = tree_height[y][0]
        heightMax_RL = tree_height[y][-1]

        for x in range(1,columns-1):

            # Left to Right Search
            if int(tree_height[y][x]) > int(heightMax_LR):
                LRSearch[y][x] = 1
                heightMax_LR = tree_height[y][x]

            # Right to Left Search
            if int(tree_height[y][(columns-1)-x]) > int(heightMax_RL):
                RLSearch[y][(columns-1)-x] = 1
                heightMax_RL = tree_height[y][(columns-1)-x]

    for x in range(1,columns-1):

        heightMax_TB = tree_height[0][x]
        heightMax_BT = tree_height[-1][x]

        for y in range(1,rows-1):

            # Top to Bottom Search
            if int(tree_height[y][x]) > int(heightMax_TB):
                TBSearch[y][x] = 1
                heightMax_TB = tree_height[y][x]

            # Bottom to Top Search
            if int(tree_height[(rows-1)-y][x]) > int(heightMax_BT):
                BTSearch[(rows-1)-y][x] = 1
                heightMax_BT = tree_height[(rows-1)-y][x]

    for y in range(1,rows-1):
        for x in range(1,columns-1):

            if LRSearch[y][x] == 1 or RLSearch[y][x] == 1 or TBSearch[y][x] == 1 or BTSearch[y][x] == 1:
                Search[y][x] = 1

print(Search)     

count = np.count_nonzero(Search == 1)
edgeCount = (((2*rows)+(2*columns))-4)
totalCount = count + edgeCount
print(totalCount)