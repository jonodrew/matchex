import csv

with open('postings.csv','rb') as f:
    reader = csv.reader(f)
    preferences = list(reader)
    #print(preferences)

with open('candidates.csv','rb') as f:
    reader = csv.reader(f)
    candidates = list(reader)
    #print(candidates)

def match(p,c):
    score = 0
    #p1 = preferences[0][0]
    #c1 = candidates[8][25]
    if p == c:
        score += 1
    else:
        score
    print(score)
p = preferences[0][0]
c = candidates[8][25]
match(p,c)
