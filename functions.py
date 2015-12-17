import numpy as np
import classes

#function finds security clearance and valorises it
score = 0
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

#function ss anchor match

def matchAnchor(skill):
    anchorMatch = []
    for anchor in anchorSkill:
        s = 0
        if anchor in items:
            score += 1.5
        else:
            score += 0.0
        #add s to this b's anchor match list
        anchorMatch.append(s)
    #add b's anchor match list to the global matrix
    anchorMatrix.append(anchorMatch)
"""
#function ss department match
def matchDept(candDept,
Dept):
    #for each item in the list of a departments...
    jobMatch = []
    if candDept
        jobMatch.append(s)
    deptMatrix.append(jobMatch)
"""

def matchDept(p,c,s):
    score = 0.0
    #deptMatch = []
    if p.department == c.wantedDept1:
        score += 1
    elif p.department == c.wantedDept2:
        score += .9
    elif p.department == c.wantedDept3:
        score += .8
    elif p.department == c.wantedDept4:
        score += .7
    elif p.department == c.wantedDept5:
        score += .6
    elif p.department == c.wantedDept6:
        score += .5
    elif p.department == c.wantedDept7:
        score += .4
    elif p.department == c.wantedDept8:
        score += .3
    elif p.department == c.wantedDept9:
        score += .2
    elif p.department == c.wantedDept10:
        score += .1
    else:
        score += 0
    return(score)
