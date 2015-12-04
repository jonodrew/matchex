import csv

with open('postings.csv','rb') as f:
    reader = csv.reader(f)
    postings = list(reader)
    #print(preferences)

with open('candidates.csv','rb') as f:
    reader = csv.reader(f)
    candidates = list(reader)
    #print(candidates)
#for values in candidates:


matrix = []
def match(p,c):
    score = 0
    if p == c:
        score += 1
    else:
        score
    matrix.append(score)

p = postings[0][1]
c = candidates[7][8]
for list in postings:
        match(p,c)
print(matrix)
