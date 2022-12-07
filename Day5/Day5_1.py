class Stack(object):

    def __init__(self, param):
        self.list = param

    def pop(self):
        return self.list.pop()

    def push(self, item):
        self.list.append(item)

    def peek(self):
        return self.list[-1]

def moveCrate(count,fromStack,toStack):
    tempStack = Stack([])
    for x in range(count):
        item = dict[fromStack].pop()
        tempStack.push(item)

dict = {
    1: Stack(['R','N','F','V','L','J','S','M']),
    2: Stack(['P','N','D','Z','F','J','W','H']),
    3: Stack(['W','R','C','D','G']),
    4: Stack(['N','B','S']),
    5: Stack(['M','Z','W','P','C','B','F','N']),
    6: Stack(['P','R','M','W']),
    7: Stack(['R','T','N','G','L','S','W']),
    8: Stack(['Q','T','H','F','N','B','V']),
    9: Stack(['L','M','H','Z','N','F']),
}

if __name__ == '__main__':
    input = open('input.txt').read().split('\n')
    for line in input:
        x = line.split(' ')
        count = int(x[1])
        fromStack = int(x[3])
        toStack = int(x[5])
        moveCrate(count,fromStack,toStack)

    for stack in dict:
        print(dict[stack].peek(), end="")