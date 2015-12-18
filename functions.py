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
        score += 3.0
    if p.anchor == c.wantedAnchor2:
        score += 1.5
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
    candidate_dept = (c.wantedDept1,c.wantedDept2,c.wantedDept3,c.wantedDept4,
    c.wantedDept5,c.wantedDept6,c.wantedDept7,c.wantedDept8,c.wantedDept9,
    c.wantedDept10)
    value = 1.0
    for dept in candidate_dept:
        if p.department == dept:
            score += value
        else:
            value -= 0.1
    return(score)

def matchCompetency(p,c):
    score = 0.0
    candidate_competencies = (c.wantedComp1,c.wantedComp2,c.wantedComp3)
    posting_competencies = (p.competency1,p.competency2,p.competency3)
    for comp in posting_competencies:
        if comp in candidate_competencies:
            score += 3
    return(score)

def matchSecurity(p,c):
    pass

def matchSkill(p,c):
    score = 0.0
    posting_skill = (p.skill1, p.skill2)
    candidate_skill = [c.wantedSkill1, c.wantedSkill2]
    for skill in posting_skill:
        if skill == candidate_skill[0]:
            score += 1
        elif skill == candidate_skill[1]:
            score += 0.5
        else:
            score = 0
    return score
