import csv

with open('input.txt') as f:
    input = f.read()

input = input.split("\n\n")
input = [lines.split('\n') for lines in input]

Score = 0

for rows in input:
    for rounds in rows:
        print(rounds)
        
        if "X" in rounds: # We play Rock
            Score = Score + 1
            if "A" in rounds: # They play Rock
                Score = Score + 3 # We drew!
            elif "B" in rounds: # They play Paper
                Score = Score + 0 # We lost!
            elif "C" in rounds: # They play Scissors
                Score = Score + 6 # We won!

        if "Y" in rounds: # We play Paper
            Score = Score + 2
            if "A" in rounds: # They play Rock
                Score = Score + 6 # We won!
            elif "B" in rounds: # They play Paper
                Score = Score + 3 # We drew!
            elif "C" in rounds: # They play Scissors
                Score = Score + 0 # We lost!

        if "Z" in rounds: # We play Scissors
            Score = Score + 3  
            if "A" in rounds: # They play Rock
                Score = Score + 0 # We lost!
            elif "B" in rounds: # They play Paper
                Score = Score + 6 # We won!
            elif "C" in rounds: # They play Scissors
                Score = Score + 3 # We drew!
                
print(Score)


