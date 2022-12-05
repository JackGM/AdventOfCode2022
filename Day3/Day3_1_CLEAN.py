def process_line(line):
    halfLength = (len(line)) // 2
    start = line[0:halfLength]
    end = line[halfLength:]

    for letter in start:
        if letter in end:
            if letter <= 'Z':
                priority = ord(letter) - ord('A') + 27
            else:
                priority = ord(letter) - ord('a') + 1
            return priority
    return 0

if __name__ == '__main__':
    input = open('input.txt').read().split('\n')
    sum = 0
    for line in input:
        sum += process_line(line)
    print(sum)