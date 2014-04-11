import random


print "Welcome to UNOwen's Amazing Coin Guessing Game!"
f = open("HighScore.txt", "r+")
HighScore = f.read()
print "\n\tThe Current High Score is: " + HighScore
print "\n"
score = 0
correct = True
while correct:
    Guess =  raw_input("Predict [H]eads or [T]ails| ").lower
    flip = random.choice(["h","t"])
    if flip == Guess and flip == "h":
        score + 1
        print "The result is heads. Your score is| " + str(score)
        correct = 1
    elif flip == Guess and flip == "t":
        score + 1
        print "The result is tails. Your score is| " + str(score)
        correct = 1
    elif flip != Guess and flip == "h":
        print "The result is heads. You lost. Your final score is| " + str(score)
        correct = 0
    else:
        print "The result is tails. You lost. Your final score is| " + str(score)
        correct = 0
if HighScore < score:
    f.seek(0)
    f.write(str(score))
    f.seek(0)
    print "Your score|", score, "\tHigh Score|", score
else:
    print "Your score|", score, "\tHigh Score|", HighScore