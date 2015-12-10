import csv
import numpy as np
import itertools
from munkres import Munkres, print_matrix
import sys

with open('/Users/java_jonathan/postings.csv','r') as f:
#with open('/Users/Jonathan/Google Drive/CPD/Python/postings.csv','r') as f:
    reader = csv.reader(f)
    postings = list(reader)
    #print(preferences)
#print(postings)
#split up files into relative blocks
postCode = [lists[0] for lists in postings]
postDept = [lists[1] for lists in postings]
postAnchor = [lists[2] for lists in postings]
postSkills = [lists[3:5] for lists in postings]
postLocation = [lists[5] for lists in postings]
postCompetencies = [lists[7:10] for lists in postings]
postSecurity = [lists[10] for lists in postings]


#with open('/Users/Jonathan/Google Drive/CPD/Python/candidates.csv','r') as f:
with open('/Users/java_jonathan/candidates.csv','r') as f:
    reader = csv.reader(f)
    candidates = list(reader)
    #print(candidates)
#for values in candidates:

candName = [lists [0:1] for lists in candidates]

chain = itertools.chain(*candName)
candName = list((chain))
candScore = {item: [] for item in candName}

candDept = [lists[14:24] for lists in candidates]
candAnchor = [lists[7:10:2] for lists in candidates]
candSkills = [lists[3:5] for lists in candidates]
candLocation = [lists[5] for lists in candidates]
candCompetencies = [lists[7:10] for lists in candidates]
candSecurity = [lists[27] for lists in candidates]


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
            score += 1.5
        else:
            score += 0.0
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
            score += 0.0
        jobMatch.append(score)
    deptMatrix.append(jobMatch)

def matchSec():
    secMatch = []
    for pSec in postSecurity:
        score = 0
        if pSec >= cSec:
            score += 1.0
        else:
            score -= 0.0
        secMatch.append(score)
    secMatrix.append(secMatch)

deptMatrix = []
for depts in candDept:
    matchDept()

anchorMatrix = []
for items in candAnchor:
    matchAnchor()

secMatrix = []
for cSec in candSecurity:
    matchSec()
#turn lists of lists into np matrices

deptMatrix = np.matrix(deptMatrix)
anchorMatrix = np.matrix(anchorMatrix)
secMatrix = np.matrix(secMatrix)
totalMatrix = deptMatrix + anchorMatrix + secMatrix

#now to select each job row:





#print(totalMatrix.T)

#gives first column ie candidate a
a=totalMatrix[:,[0]]
#b = totalMatrix[:,[0]]
#print(a)
#converts 1D matrix to list for ease
a = np.array(a).tolist()
#print(a)
#creates list called output containing rank of score
output = [0] * len(a)
for i, x in enumerate(sorted(range(len(a)), key=lambda y: a[y])):
    output[x] = i
print(output)
#creates tuples of rank, job and appends to list
jobRank = []
for rank, b in zip(output, postCode):
    jobScore = (rank,b)
    list(jobScore)
    jobRank.append(jobScore)
print(jobRank)

"""
output = [0] * len(a)
for i, x in enumerate(sorted(range(len(a)), key=lambda y: a[y])):
    output[x] = i
print(output)
"""
#print(a)
jobRank = sorted(jobRank, reverse=False)
print(jobRank)
print('For candidate a, the best position is %s') % (jobRank[0][1])
