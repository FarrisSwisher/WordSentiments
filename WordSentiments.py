#Word Sentiments
#submitted February 2018
#last edited 06/08/20 (updated to work in Python 3)
#
#Use sentiment lexicon to analyze script group a or b
#Output is a bar chart of total negative, weak neg, neutral, weak pos and positive words




#Sources:

#Python docs: glob - Unix style pathname pattern expansion
#https://docs.python.org/2/library/glob.html


from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import re
import glob



## read sentiment lexicon
data = open("sentiment_lex.csv", "r")
data = data.read()
data = data.split()



## make sentiment lexicon usable
slex = {}
for line in data:
    line = line.split(",")
    slex[line[0]] = np.float32(line[1])



## negative, weak neg, neutral, weak positive, positive dictionaries
## using sentiment lexicon
neg = {}
wneg = {}
neut = {}
wpos = {}
pos = {}
for key, value in slex.items():
    if value < -0.6:
        neg[key] = value
    if value >= -0.6 and value < -0.2:
        wneg[key] = value
    if value >= -0.2 and value <= 0.2:
        neut[key] = value
    if value > 0.2 and value <= 0.6:
        wpos[key] = value
    if value > 0.6:
        pos[key] = value

## word count for each category
negCount = 0
wnCount = 0
neutCount = 0
wpCount = 0
posCount = 0


## prompt user for A script or B script
choice = input("Pick which series for which you wish to view script analysis (A or B):\n")

print ("\n\n")
# if user chooses A
if choice.lower() == "a":
    aScript = glob.glob('a1*')
    Awords = []
    for file in aScript:
        data = open(file, "r")
        data = data.read()
        data = re.sub(r'\W+', " ", data)
        data = data.split(" ")
        for word in data:
            if not word.isalpha() or len(word) == 1 or word == word.upper():
                continue
            Awords.append(word.lower())

    print ("Calculating negative word count. . .")
    for word in Awords:
        for key in neg.keys():
            if word == key:
                negCount += 1
    print (negCount)
    print ("\n")

    print ("Calculating weak negative word count. . .")
    for word in Awords:
        for key in wneg.keys():
            if word == key:
                wnCount += 1
    print (wnCount)
    print ("\n")

    print ("Calculating neutral word count. . .")
    for word in Awords:
        for key in neut.keys():
            if word == key:
                neutCount += 1
    print (neutCount)
    print ("\n")

    print ("Calculating weak positive word count. . .")
    for word in Awords:
        for key in wpos.keys():
            if word == key:
                wpCount += 1
    print (wpCount)
    print ("\n")

    print ("Calculating positive word count. . .")
    for word in Awords:
        for key in pos.keys():
            if word == key:
                posCount += 1
    print (posCount)
    print ("\n")

    x_vals = ["Neg", "W.Neg", "Neut", "W.Pos", "Pos"]
    y_vals = [negCount, wnCount, neutCount, wpCount, posCount]
    y_vals = np.log10(y_vals)

    mplot.bar(range(0, len(y_vals)), y_vals)
    mplot.xticks(range(0, len(x_vals)), x_vals)
    mplot.xlabel("Sentiment")
    mplot.ylabel("log10 Word Count")
    mplot.title("Sentiment Analysis for Series A")
    mplot.show()


## if user chooses B
elif choice.lower() == "b":
    bScript = glob.glob('bg*')
    Bwords = []
    for file in bScript:
        data = open(file, "r")
        data = data.read()
        data = re.sub(r'\W+', " ", data)
        data = data.split(" ")
        for word in data:
            if not word.isalpha() or len(word) == 1 or word == word.upper():
                continue
            Bwords.append(word.lower())

    print ("Calculating negative word count. . .")
    for word in Bwords:
        for key in neg.keys():
            if word == key:
                negCount += 1
    print (negCount)
    print ("\n")

    print ("Calculating weak negative word count. . .")
    for word in Bwords:
        for key in wneg.keys():
            if word == key:
                wnCount += 1
    print (wnCount)
    print ("\n")

    print ("Calculating neutral word count. . .")
    for word in Bwords:
        for key in neut.keys():
            if word == key:
                neutCount += 1
    print (neutCount)
    print ("\n")

    print ("Calculating weak positive word count. . .")
    for word in Bwords:
        for key in wpos.keys():
            if word == key:
                wpCount += 1
    print (wpCount)
    print ("\n")

    print ("Calculating positive word count. . .")
    for word in Bwords:
        for key in pos.keys():
            if word == key:
                posCount += 1
    print (posCount)
    print ("\n")

    x_vals = ["Neg", "W.Neg", "Neut", "W.Pos", "Pos"]
    y_vals = [negCount, wnCount, neutCount, wpCount, posCount]
    y_vals = np.log10(y_vals)

    mplot.bar(range(0, len(y_vals)), y_vals)
    mplot.xticks(range(0, len(x_vals)), x_vals)
    mplot.xlabel("Sentiment")
    mplot.ylabel("log10 Word Count")
    mplot.title("Sentiment Analysis for Series B")
    mplot.show()

## error statement for all other potential user input
else:
    print ("Invalid user input!!!")
