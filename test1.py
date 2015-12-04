import csv

with open('postings.csv','rb') as f:
    reader = csv.reader(f)
    postings = list(reader)
    #print(preferences)
#print(postings)
#split up files into relative blocks
postDept = [lists[1] for lists in postings]
postAnchor = [lists[2] for lists in postings]
postSkills = [lists[3:5] for lists in postings]
postLocation = [lists[5] for lists in postings]
postCompetencies = [lists[7:10] for lists in postings]
postSecurity = [lists[10] for lists in postings]
"""
for lists in postings:
    dept.append(postings[0][0:1:10])
"""
#print(postDept,postSkills,postAnchor,postCompetencies,postSecurity)

with open('candidates.csv','rb') as f:
    reader = csv.reader(f)
    candidates = list(reader)
    #print(candidates)
#for values in candidates:
candDept = [lists[14:24] for lists in candidates]
candAnchor = [lists[2] for lists in candidates]
candSkills = [lists[3:5] for lists in candidates]
candLocation = [lists[5] for lists in candidates]
candCompetencies = [lists[7:10] for lists in candidates]
candSecurity = [lists[14:25] for lists in candidates]
print(candDept)

"""
matrix = []
def matchDept(p,c):
    score = 0
    if p == c:
        score += 1
    else:
        score
    return score

def match(p,c):
    score = 0
    if p == c:
        score += 1
    else:
        score


p = postings[0][1]
c = candidates[7][1]
for list in postings:
    score = 0
    #matchDept(p,c)
    #match(postings[0][2],candidates[8][9])
    matrix.append(score)
print(matrix)
print (candidates[0])
"""
