with open('input.txt') as f:
    input = f.read()

input = input.split("\n\n")
input = [lines.split('\n') for lines in input]

sum = 0

for data in input:
    for rows in data:
        halfLength = int((len(rows))/2)
        start = rows[0:halfLength]
        end = rows[halfLength:]

        for N in range(0,len(start)):
            if start[N] in end:
                print("Found Match! - ",start[N])

                if ord(start[N]) <= 90:
                    priority = ord(start[N]) - 64 # Index Upper Case from 1
                    priority = priority + 26      # Index Upper Case from 27
                else:
                    priority = ord(start[N]) - 96 # Index Lower Case from 1
                print(priority)

                break
        sum = sum + priority
print(sum)