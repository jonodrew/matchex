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

#function gives anchor match

def matchAnchor(p,c):
    score = 0.0
    if p.anchor == c.wantedAnchor:
        score += 1.7
    if p.anchor == c.wantedAnchor2:
        score += 0.8
    return(score)

def matchLocation(p,c):
    score = 0.0
    if c.restrictions == 'No' and p.location == c.wantedLocation:
        score += 1.6
    elif c.restrictions != 'No' and p.location == c.wantedLocation:
        score += 7.0
    elif c.restrictions != 'No' and p.location != c.wantedLocation:
        score -= 10.0
    return(score)

def matchDept(p,c):
    score = 0.0
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

def matchSecurity(p,c):
    pass

def matchCompetency(p,c):
    pass

def matchSkill(p,c):
    pass
