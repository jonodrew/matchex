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
competencyMatrix = []
skillMatrix = []
for list in candidatesAll:
    candidate = Candidate(*list)
    #stores score for each m posts across each candidate
    deptMatch = []
    anchorMatch = []
    locationMatch = []
    competencyMatch = []
    skillMatch = []
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
        score = matchCompetency(posting,candidate)
        #print(score)
        competencyMatch.append(score)
        score = matchSkill(posting,candidate)
        skillMatch.append(score)

    #append list to list of lists
    deptMatrix.append(deptMatch)
    anchorMatrix.append(anchorMatch)
    locationMatrix.append(locationMatch)
    competencyMatrix.append(competencyMatch)
    skillMatrix.append(skillMatch)
#convert list of lists to matrix
deptMatrix = np.matrix(deptMatrix)
anchorMatrix = np.matrix(anchorMatrix)
locationMatrix = np.matrix(locationMatrix)
competencyMatrix = np.matrix(competencyMatrix)
skillMatrix = np.matrix(skillMatrix)
totalMatrix = anchorMatrix + deptMatrix + locationMatrix + competencyMatrix \
+ skillMatrix
#at this point the matrix is structured as candidates down and jobs across
totalMatrix = np.transpose(totalMatrix)
#print(totalMatrix)
#now it's switched!
totalMatrix = np.subtract(np.amax(totalMatrix),totalMatrix)
totalMatrix = np.array(totalMatrix)

maxHappy = 12.75*10

check = []
m = Munkres()
indexes = m.compute(totalMatrix)
print_matrix(totalMatrix, msg='Lowest cost through this matrix:')
total = 0.0
for row, column in indexes:
    value = totalMatrix[row][column]
    total += value
    check.append(column+1)
    print ('(%d, %d) -> %s' % (row+1, column+1, value))
print 'total unhappiness: %s out of %d' % (total,maxHappy)

#output from excel:
correct = [1,3,5,9,10,2,4,8,6,7]

#this function tests output above against Excel:
def test(a,b):
    score = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            score += 1
        else:
            score += 0
    print('%d out of 10' % score)

test(correct,check)
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


#with open('/Users/Jonathan/Google Drive/CPD/Python/candidates.csv','r') as f:





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
# for rank, b in zip(output, postCode):
#     jobScore = (rank,b)
#     list(jobScore)
#     jobRank.append(jobScore)
# print(jobRank)


output = [0] * len(a)
for i, x in enumerate(sorted(range(len(a)), key=lambda y: a[y])):
    output[x] = i
print(output)

# #print(a)
# jobRank = sorted(jobRank, reverse=False)
# print(jobRank)
# print('For candidate a, the best position is %s') % (jobRank[0][1])
# print(candidate[0].skills)
"""
