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

with open('/Users/java_jonathan/candidates.csv','r') as f:
    reader = csv.reader(f)
    candidatesAll = list(reader)

#iterates over lists and produces the names of each candidate
for list in candidatesAll:
    candidate = Candidate(*list)
    #print(candidate.name)
    #print(candidate.priorDepartment)
for list in postingsAll:
    posting = Posting(*list)

#need to turn this into a function and move it across to functions module
deptMatrix = []
for list in candidatesAll:
    candidate = Candidate(*list)
    deptMatch = []
    for list in postingsAll:
        posting = Posting(*list)
        score = 0.0
        if posting.department == candidate.wantedDept1:
            score += 1
        elif posting.department == candidate.wantedDept2:
            score += .9
        elif posting.department == candidate.wantedDept3:
            score += .8
        elif posting.department == candidate.wantedDept4:
            score += .7
        elif posting.department == candidate.wantedDept5:
            score += .6
        elif posting.department == candidate.wantedDept6:
            score += .5
        elif posting.department == candidate.wantedDept7:
            score += .4
        elif posting.department == candidate.wantedDept8:
            score += .3
        elif posting.department == candidate.wantedDept9:
            score += .2
        elif posting.department == candidate.wantedDept10:
            score += .1
        else:
            score += 0
        print(score)
        deptMatch.append(score)
    deptMatrix.append(deptMatch)
deptMatrix = np.matrix(deptMatrix)
print(deptMatrix)
for item in deptMatrix:
    item * 2
print(deptMatrix)
"""
for list in postingsAll:
    deptMatrix = []
    posting = Posting(*list)
    for list in candidatesAll:
        deptMatch = []
        candidate = Candidate(*list)
        matchDept(posting,candidate)
        print(deptMatch)


    #print(posting.name)
    #print(posting.department)


#posting = [Posting(*postingsAll)]
#print(posting[0].anchor)
#print(posting)
#print(candidatesAll)
#print(postingsAll)
#print(postingsAll[0].name)
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
"""

#with open('/Users/Jonathan/Google Drive/CPD/Python/candidates.csv','r') as f:

"""



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
