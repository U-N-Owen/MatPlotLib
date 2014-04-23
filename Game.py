#! /usr/bin/env Python

import random as rand

print "Welcome to UNOwen's Amazing Coin Guessing Game!"
f = open("HighScore.txt", "r+")
HighScore = f.read()
print "\n\tThe Current High Score is: " + HighScore
print "\n"
score = 0
correct = True
while correct:
    Guess =  raw_input("Predict [h]eads or [t]ails| ").lower()
    while Guess != "h" and Guess != "t":
        Guess = raw_input("Please input h or t | ").lower()
    flip = rand.randint(0,1)
    if Guess == "h" and flip == 0:
        score += 1
        print "The result is heads. Your score is| " + str(score)
        correct = True
    elif Guess == "t" and flip == 1:
        score += 1
        print "The result is tails. Your score is| " + str(score)
        correct = True
    elif Guess == "t" and flip == 0:
        print "The result is heads. You lost. Your final score is| " + str(score)
        correct = False
    else:
        print "The result is tails. You lost. Your final score is| " + str(score)
        correct = False
        print Guess
if int(HighScore) < score:
    f.seek(0)
    f.write(str(score))
    print "Your score|", score, "\tHigh Score|", score
else:
    print "Your score|", score, "\tHigh Score|", HighScore