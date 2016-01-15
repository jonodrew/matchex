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
from math import sqrt

"""for use with /users/java_jonathan/postings_lge.csv and
/Users/java_jonathan/candidates_lge.csv"""

p_file = raw_input("Please enter the path for the postings file: ")
c_file = raw_input("Please enter the path for the candidate file: ")

with open(p_file,'r') as f:
#with open('/Users/Jonathan/Google Drive/CPD/Python/postings.csv','r') as f:
    reader = csv.reader(f)
    postingsAll = list(reader)

with open(c_file,'r') as f:
    reader = csv.reader(f)
    candidatesAll = list(reader)


"""create empty lists to fill with lists of lists output by iterating function
below"""
names = []
totalMatrix = []
for list in candidatesAll:
    candidate = Candidate(*list)
    names.append(candidate.name)
    n = 0
    for list in postingsAll:
        posting = Posting(*list)
        totalMatrix.append(matchDept(posting,candidate) + matchAnchor(posting,candidate)
        +matchLocation(posting,candidate) + matchCompetency(posting,candidate) +
        matchSkill(posting,candidate)+matchCohort(posting,candidate))
        n += 1
l = len(names)
names.extend([0] * (n-l))

totalMatrix.extend([0] * (n**2 - len(totalMatrix)))
totalMatrix = np.asarray(totalMatrix)

totalMatrix = np.reshape(totalMatrix,(n,-1))
#at this point the matrix is structured as candidates down and jobs across
totalMatrix = np.transpose(totalMatrix)
#now it's switched!
totalMatrix = np.subtract(np.amax(totalMatrix),totalMatrix)
totalMatrix = np.array(totalMatrix)
minSuitability = 18
check = []
result = []
m = Munkres()
indexes = m.compute(totalMatrix)
#print_matrix(totalMatrix, msg='Lowest cost through this matrix:')
total = 0.0
unhappy_candidates = 0
medium_candidates = 0
tenpc_candidates = 0
qs_candidates = 0
vs_candidates = 0
f = open('output.txt', 'w')
for row, column in indexes:
    if column < l:
        value = totalMatrix[row][column]
        if value > minSuitability*0.9:
            tenpc_candidates += 1
        elif value > minSuitability*0.75:
                medium_candidates += 1
        elif value > minSuitability/2:
            unhappy_candidates += 1
        elif value > minSuitability*0.25:
            qs_candidates += 1
        elif value > minSuitability*0.1:
            vs_candidates += 1
        total += value
        check.append(column+1)
        result.append((row,column))
        f.write('For candidate %s: \nOptimal position: %d (score %s)\n'
        % (names[column], column+1, value))
    else:
        pass
globalSatisfaction = 100*(1-(total/(l*minSuitability)))
print('Global satisfaction: %.2f%%' % globalSatisfaction)
print('Candidates who are more than 90%% suitable: %d' % vs_candidates)
print('Candidates who are more than 75%% suitable: %d' % qs_candidates)
print('Candidates who are more than 50%% suitable: %d' % (l-unhappy_candidates))
print('Candidates who are more than 75%% unsuitable: %d' % medium_candidates)
print('Candidates who are more than 90%% unsuitable: %d' % tenpc_candidates)

#output from excel:
correct = [1,3,5,9,10,2,4,8,6,7]

#this function tests output above against Excel:
#test(correct,check)
topMatrix = topFive(names,totalMatrix)
#print(topMatrix)

np.savetxt('/Users/java_jonathan/test.csv',topMatrix, fmt='%s', delimiter=',',
newline='\n', header='', footer='', comments='# ')
np.savetxt('/Users/java_jonathan/test2.csv',totalMatrix, fmt='%s', delimiter=',',
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
