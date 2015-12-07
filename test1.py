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
candSecurity = [lists[27] for lists in candidates]
#print(candAnchor)
#print(candName)

#print(candSecurity)
def secValue(clearance):
    for n,i in enumerate(clearance):
        if i == 'SC':
            clearance[n] = 3
        elif i == 'DV':
            clearance[n] = 4
        elif i == 'CTC':
            clearance[n] = 2
        else:
            clearance[n] = 1
secValue(candSecurity)
secValue(postSecurity)
#print(candSecurity)

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

def matchSec():
    secMatch = []
    for pSec in postSecurity:
        score = 0
        if pSec >= cSec:
            score += 2
        else:
            score -= 10
        secMatch.append(score)
    secMatrix.append(secMatch)

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

secMatrix = []
for cSec in candSecurity:
    matchSec()

deptMatrix = np.matrix(deptMatrix)
anchorMatrix = np.matrix(anchorMatrix)
secMatrix = np.matrix(secMatrix)
print(secMatrix)
#print(anchorMatrix + deptMatrix)
"""
#print(matrix)
#print(candDept,postDept)

#import numpy as np
"""
