import csv
import numpy as np
import itertools
from munkres import Munkres, print_matrix
import sys
from classes import *
from functions import *

with open('/Users/java_jonathan/postings.csv','r') as f:
#with open('/Users/Jonathan/Google Drive/CPD/Python/postings.csv','r') as f:
    reader = csv.reader(f)
    postingsAll = list(reader)
    #print(postingsAll)
    #print(postingsAll)
with open('/Users/java_jonathan/candidates_lge.csv','r') as f:
    reader = csv.reader(f)
    candidatesAll = list(reader)

#iterates over lists and produces the names of each candidate
for list in candidatesAll:
    candidate = Candidate(*list)
    print(candidate.name)
    print(candidate.priorDepartment)
#posting = [Posting(*postingsAll)]
#print(posting[0].anchor)
#print(posting)
#print(candidatesAll)
#print(postingsAll)
#print(postingsAll[0].name)
    #print(preferences)
#print(postings)
#split up files into relative blocks
"""
postCode = [lists[0] for lists in postings]
postDept = [lists[1] for lists in postings]
postAnchor = [lists[2] for lists in postings]
postSkills = [lists[3:5] for lists in postings]
postLocation = [lists[5] for lists in postings]
postCompetencies = [lists[7:10] for lists in postings]
postSecurity = [lists[10] for lists in postings]
"""

#with open('/Users/Jonathan/Google Drive/CPD/Python/candidates.csv','r') as f:

    #print(candidates)
#for values in candidates:
#print(candidates)
#print(postingsAll)

"""
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


secValue(candSecurity)
secValue(postSecurity)
matchAnchor()
#print(candSecurity)
"""

"""

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


output = [0] * len(a)
for i, x in enumerate(sorted(range(len(a)), key=lambda y: a[y])):
    output[x] = i
print(output)

#print(a)
jobRank = sorted(jobRank, reverse=False)
print(jobRank)
print('For candidate a, the best position is %s') % (jobRank[0][1])
print(candidate[0].skills)
"""
