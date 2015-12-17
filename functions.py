import numpy as np
import classes

#function finds security clearance and valorises it
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

#function scores anchor match

def matchAnchor(skill):
    anchorMatch = []
    for anchor in anchorSkill:
        score = 0
        if anchor in items:
            score += 1.5
        else:
            score += 0.0
        #add score to this b's anchor match list
        anchorMatch.append(score)
    #add b's anchor match list to the global matrix
    anchorMatrix.append(anchorMatch)
"""
#function scores department match
def matchDept(candDept,
Dept):
    #for each item in the list of a departments...
    jobMatch = []
    if candDept
        jobMatch.append(score)
    deptMatrix.append(jobMatch)
"""

def matchDept(a,b):

    score = 0.0
    if a.department == b.wantedDept1:
        score += 1
    elif a.department == b.wantedDept2:
        score += .9
    elif a.department == b.wantedDept3:
        score += .8
    elif a.department == b.wantedDept4:
        score += .7
    elif a.department == b.wantedDept5:
        score += .6
    elif a.department == b.wantedDept6:
        score += .5
    elif a.department == b.wantedDept7:
        score += .4
    elif a.department == b.wantedDept8:
        score += .3
    elif a.department == b.wantedDept9:
        score += .2
    elif a.department == b.wantedDept10:
        score += .1
    else:
        score += 0
    return score
    print(score)
    deptMatch.append(score)
