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
def matchAnchor(anchorSkill):
    anchorMatch = []
    for anchor in anchorSkill:
        score = 0
        if anchor in items:
            score += 1.5
        else:
            score += 0.0
        #add score to this candidate's anchor match list
        anchorMatch.append(score)
    #add candidate's anchor match list to the global matrix
    anchorMatrix.append(anchorMatch)

#function scores department match
def matchDept():
    #for each item in the list of posting departments...
    jobMatch = []
    for dept in postDept:
        score = 0
        if dept in depts:
            score += 1
        else:
            score += 0.0
        jobMatch.append(score)
    deptMatrix.append(jobMatch)
