import csv
import numpy as np
import itertools
from munkres import Munkres, print_matrix, make_cost_matrix
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

"""create empty lists to fill with lists of lists output by iterating function
below"""
deptMatrix = []
anchorMatrix = []
locationMatrix = []
for list in candidatesAll:
    candidate = Candidate(*list)
    #stores score for each m posts across each candidate
    deptMatch = []
    anchorMatch = []
    locationMatch = []
    for list in postingsAll:
        posting = Posting(*list)
        #initisalise postings
        score = matchDept(posting,candidate)
        #append score to candidate's list
        deptMatch.append(score)
        score = matchAnchor(posting,candidate)
        anchorMatch.append(score)
        score = matchLocation(posting,candidate)
        locationMatch.append(score)

    #append list to list of lists
    deptMatrix.append(deptMatch)
    anchorMatrix.append(anchorMatch)
    locationMatrix.append(locationMatch)
#convert list of lists to matrix
deptMatrix = np.matrix(deptMatrix)
anchorMatrix = np.matrix(anchorMatrix)
locationMatrix = np.matrix(locationMatrix)
print(deptMatrix)
print(anchorMatrix)
totalMatrix = anchorMatrix + deptMatrix + locationMatrix
print(totalMatrix)
totalMatrix = np.subtract(10,totalMatrix)
totalMatrix = np.array(totalMatrix)
print(totalMatrix)



m = Munkres()
indexes = m.compute(totalMatrix)
print_matrix(totalMatrix, msg='Lowest cost through this matrix:')
total = 0.0
for row, column in indexes:
    value = totalMatrix[row][column]
    total += value
    print ('(%d, %d) -> %s' % (row, column, value))
print 'total happiness: %s out of 100' % total



"""
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
