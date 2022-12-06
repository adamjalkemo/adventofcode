from pathlib import Path

input = Path("input.txt").read_text().strip().split("\n")

# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that them say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

#The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

#The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).




translation = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}


shape_score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

outcome_score = {
    "Loss": 0,
    "Draw": 3,
    "Win": 6,
}

winning_outcomes = {
    "Scissors": "Paper",
    "Paper": "Rock",
    "Rock": "Scissors"
}

losing_outcomes = {v: k for k, v in winning_outcomes.items()}

matches = [x.split(" ") for x in input]
strategies = [[translation[them], translation[me]] for them, me in matches]


score = 0
for them, me in strategies:
    score += shape_score[me]
    if them == me:
        score += outcome_score["Draw"]
    else:
        if them == winning_outcomes[me]:
            score += outcome_score["Win"]

print("pt1: ", score)

outcome_translation = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win"
}

strategies = [[translation[them], outcome_translation[me]] for them, me in matches]

score = 0
for them, outcome in strategies:
    score += outcome_score[outcome]
    if outcome == "Draw":
        me = them
    else:
        if outcome == "Win":
            me = losing_outcomes[them]
        else:
            me = winning_outcomes[them]
    score += shape_score[me]

print("pt2: ", score)

