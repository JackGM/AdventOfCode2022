class Stack(object):
    
    def __init__(self, param):
        self.list = param

    def pop(self):
        return self.list.pop()

    def push(self, item):
        self.list.append(item)

    def peek(self):
        return self.list[-1]

    def clear(self):
        self.list.clear()

class Node():

    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def addChild(self,child):
        self.children.append(Node(child,self))

    def findChild(self,childName):
        for child in self.children:
            if child.name == childName:
                return child

    def addFile(self,filename,size):
        self.files.append(File(filename,int(size)))

    def traverse(self):
        sum = 0
        global smallDir
        for child in self.children:
            sum += child.traverse()  
        for file in self.files:
            sum += file.size
        if sum < 100000:
            smallDir += sum
        return sum

class File():

    def __init__(self, filename, size):
        self.name = filename
        self.size = size

location = Stack([])                                        # Keep Track of Location within the Tree!       
root = Node("/", None)                                      # Create the Root Node.
smallDir = 0

if __name__ == '__main__':

    input = open('input.txt').read().split('\n')

    for line in input:

        if "$ cd .." in line:                               # Go to Parent Directory
            location.pop()                                  # Remove Child Directory from Location Stack.
            print("Go to Parent Directory - ",location.peek().name)

        elif "$ cd /" in line:                              # Return to Root Directory.
            print("Return to Root")
            location.clear()                                # Clears all Nodes from Location Stack.
            location.push(root)                             # Adds the Root Node to the Location Stack.

        elif "$ cd" in line:
            childName = line.split(" ")[-1]                 # Find Name of Child Directory.
            print("Go to Child Directory - ",childName)
            parent = location.peek()                        # Find Name of Parent Directory.    
            location.push(parent.findChild(childName))      # Add Child Node to Location Stack.

        elif "$ ls" in line:
            print("List Files in Directory")

        elif "dir" in line:
            childName = line.split(" ")[1]                  # Find Name of Child Directory.
            print("Add Directory - ",childName)
            parent = location.peek()                        # Find Name of Parent Directory.
            parent.addChild(childName)                      # Add Child Directory.  

        else:
            name = line.split(" ")[1]                       # Find Name of File.
            print("Add File - ",name)
            size = line.split(" ")[0]                       # Find Size of File.
            parent = location.peek()                        # Find Name of Parent Directory.
            parent.addFile(name,size)                       # Add File.

    print("Total Size - ",root.traverse())
    print("Total of Small Directories - ",smallDir)