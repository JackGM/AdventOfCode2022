import csv

with open('input.txt') as f:
    input = f.read()

input = input.split("\n\n")
input = [lines.split('\n') for lines in input]

Score = 0

Win = 6
Draw = 3
Lose = 0

Rock = 1
Paper = 2
Scissors = 3

for rows in input:
    for rounds in rows:
        print(rounds)

        if "A" in rounds: # They play Rock
            if "X" in rounds: # We need to lose
                Score = Score + Lose
                Score = Score + Scissors # Lose to Rock
            if "Y" in rounds: # We need to draw
                Score = Score + Draw
                Score = Score + Rock # Draw to Rock
            if "Z" in rounds: # We need to win
                Score = Score + Win
                Score = Score + Paper # Win against Rock

        if "B" in rounds: # They play Paper
            if "X" in rounds: # We need to lose
                Score = Score + Lose
                Score = Score + Rock # Lose to Paper
            if "Y" in rounds: # We need to draw
                Score = Score + Draw
                Score = Score + Paper # Draw to Paper
            if "Z" in rounds: # We need to win
                Score = Score + Win
                Score = Score + Scissors # Win against Paper

        if "C" in rounds: # They play Scissors
            if "X" in rounds: # We need to lose
                Score = Score + Lose
                Score = Score + Paper # Lose to Scissors
            if "Y" in rounds: # We need to draw
                Score = Score + Draw
                Score = Score + Scissors # Draw to Scissors
            if "Z" in rounds: # We need to win
                Score = Score + Win
                Score = Score + Rock # Win against Scissors

print(Score)