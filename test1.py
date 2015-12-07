import csv
import numpy as np

with open('/Users/Jonathan/Google Drive/CPD/Python/postings.csv','r') as f:
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

with open('/Users/Jonathan/Google Drive/CPD/Python/candidates.csv','r') as f:
    reader = csv.reader(f)
    candidates = list(reader)
    #print(candidates)
#for values in candidates:

candName = [lists [0:1] for lists in candidates]
candDept = [lists[14:24] for lists in candidates]
candAnchor = [lists[7:10:2] for lists in candidates]
candSkills = [lists[3:5] for lists in candidates]
candLocation = [lists[5] for lists in candidates]
candCompetencies = [lists[7:10] for lists in candidates]
candSecurity = [lists[14:25] for lists in candidates]
#print(candAnchor)
#print(candName)


def matchAnchor():
    anchorMatch = []
    for anchor in postAnchor:
        score = 0
        if anchor in items:
            score += 1
        else:
            score += 0
        anchorMatch.append(score)
    anchorMatrix.append(anchorMatch)

def matchDept():
    #score = 0
    #for each item in the list of posting departments...
    jobMatch = []
    for dept in postDept:
        score = 0
        if dept in depts:
            score += 1
        else:
            score += 0
        jobMatch.append(score)
    deptMatrix.append(jobMatch)


import itertools
chain = itertools.chain(*candName)
candName = list((chain))
candScore = {item: [] for item in candName}

#for each chunk of "preferred departments..."
deptMatrix = []
for depts in candDept:
    matchDept()

anchorMatrix = []
for items in candAnchor:
    matchAnchor()


deptMatrix = np.matrix(deptMatrix)
anchorMatrix = np.matrix(anchorMatrix)
print(anchorMatrix + deptMatrix)
"""
#print(matrix)
#print(candDept,postDept)

#import numpy as np
"""
