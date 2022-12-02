import csv

with open('input.txt') as f:
    input = f.read()

input = input.split("\n\n")
input = [lines.split('\n') for lines in input]

No1 = 0
No2 = 0
No3 = 0

for rows in input:
    print(rows)
    result = sum(int(x) for x in rows)
    print(result)

    if result >= No1:
        No3 = No2
        No2 = No1
        No1 = result
    elif result >= No2:
        No3 = No2
        No2 = result
    elif result >= No3:
        No3 = result

    print("#1 = ", No1)
    print("#2 = ", No2)
    print("#3 = ", No3)

Total = No1 + No2 + No3
print("Total =", Total)