from __future__ import division
from timeit import default_timer as timer
start = timer()
import csv
import numpy as np
import itertools
from munkres import Munkres, print_matrix, make_cost_matrix
import sys
from classes import *
from functions import *



with open('/Users/java_jonathan/postings_lge.csv','r') as f:
#with open('/Users/Jonathan/Google Drive/CPD/Python/postings.csv','r') as f:
    reader = csv.reader(f)
    postingsAll = list(reader)

with open('/Users/java_jonathan/candidates_lge.csv','r') as f:
    reader = csv.reader(f)
    candidatesAll = list(reader)


"""create empty lists to fill with lists of lists output by iterating function
below"""
deptMatrix = []
anchorMatrix = []
locationMatrix = []
competencyMatrix = []
skillMatrix = []
names = []
for list in candidatesAll:
    candidate = Candidate(*list)
    names.append(candidate.name)
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
deptMatrix = np.multiply(np.matrix(deptMatrix),1)
anchorMatrix = np.matrix(anchorMatrix)
locationMatrix = np.matrix(locationMatrix)
competencyMatrix = np.matrix(competencyMatrix)
skillMatrix = np.matrix(skillMatrix)
totalMatrix = anchorMatrix + deptMatrix + locationMatrix + competencyMatrix \
+ skillMatrix
#at this point the matrix is structured as candidates down and jobs across
totalMatrix = np.transpose(totalMatrix)
#now it's switched!
totalMatrix = np.subtract(np.amax(totalMatrix),totalMatrix)
totalMatrix = np.array(totalMatrix)

minSuitability = np.amax(totalMatrix)
print('Lowest satisfaction with role: %s' % minSuitability)
check = []
result = []
m = Munkres()
indexes = m.compute(totalMatrix)
print_matrix(totalMatrix, msg='Lowest cost through this matrix:')
total = 0.0
unhappy_candidates = 0
medium_candidates = 0
tenpc_candidates = 0
for row, column in indexes:
    value = totalMatrix[row][column]
    if value > minSuitability/2:
        unhappy_candidates += 1
    elif value > minSuitability*0.33:
        medium_candidates += 1
    elif value > minSuitability*0.1:
        tenpc_candidates += 1
    total += value
    check.append(column+1)
    result.append((row,column))
    print ('For position %d: \nOptimal candidate: %s (score %s)'
    % (row+1, candidatesAll[row][0], value))
globalSatisfaction = 100*(1-(total/(len(totalMatrix)*minSuitability)))
print('Global satisfaction: %.2f%%' % globalSatisfaction)
print('Candidates who are less than 50%% suitable: %d' % unhappy_candidates)
print('Candidates who are less than 33%% suitable: %d' % medium_candidates)
print('Candidates who are less than 10%% suitable: %d' % tenpc_candidates)
#output from excel:
correct = [1,3,5,9,10,2,4,8,6,7]
"""
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
num = 5
top = np.argpartition(totalMatrix,num, axis = 1)[:,:num]
topFive = np.array(totalMatrix[np.arange(totalMatrix.shape[0])[:, None],top])
topMatrix = np.array(topMatch(totalMatrix,top,names))
topMatrix = np.dstack((topMatrix,topFive))
print(topMatrix)
np.savetxt('test.csv',topMatrix, fmt='%s', delimiter=',',
newline='\n', header='', footer='', comments='# ')
np.savetxt('test2.csv',totalMatrix, fmt='%s', delimiter=',',
newline='\n', header='', footer='', comments='# ')
end = timer()
print(end-start)
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
