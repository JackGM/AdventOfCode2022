import numpy as np

if __name__ == '__main__':
    input = open('D:\AdventOfCode\Day8\input.txt').read().split('\n')
    rows = len(input)
    columns = len(input[0])
    tree_height = np.zeros([rows,columns], dtype = int)
    scoreScenic = 0
    scoreScenicMax = 0

    for row_index,line in enumerate(input):
        for column_index,height in enumerate(line):
            tree_height[row_index][column_index] = height

    for y in range(1,rows-1):
        for x in range(1,columns-1):

            scoreUp = 0
            scoreDown = 0
            scoreLeft = 0
            scoreRight = 0

            # Look Up
            for j in range(y-1,-1,-1):   
                if (tree_height[j][x] >= tree_height[y][x]) or (j == 0):
                    scoreUp += 1
                    break
                elif tree_height[j][x] < tree_height[y][x]:
                    scoreUp += 1

            # Look Down
            for j in range(y+1,rows):   
                if (tree_height[j][x] >= tree_height[y][x]) or (j == rows):
                    scoreDown += 1
                    break
                elif tree_height[j][x] < tree_height[y][x]:
                    scoreDown += 1

            # Look Left
            for i in range(x-1,-1,-1):   
                if (tree_height[y][i] >= tree_height[y][x]) or (i == 0):
                    scoreLeft += 1
                    break
                elif tree_height[y][i] < tree_height[y][x]:
                    scoreLeft += 1

            # Look Right
            for i in range(x+1,columns):   
                if (tree_height[y][i] >= tree_height[y][x]) or (i == columns):
                    scoreRight += 1
                    break
                elif tree_height[y][i] < tree_height[y][x]:
                    scoreRight += 1

            scoreScenic = scoreUp * scoreDown * scoreLeft * scoreRight
            if scoreScenic > scoreScenicMax:
                scoreScenicMax = scoreScenic
                
    print(scoreScenicMax)
