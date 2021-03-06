"""to avoid very lengthy code that covers every permutation of strings SC, DV etc
we should valorise these levels
def security_value(self,level):
    if level == 'SC':
        self.security = 3
    elif level == 'DV':
        self.security = 4
    else:
"""
class Candidate(object):

    def __init__(self, name, priorDepartment, priorAnchor, priorSkill1,
    priorSkill2, priorLocation, XX, wantedAnchor, wantedSkill1,
    wantedAnchor2,wantedSkill2,wantedComp1,wantedComp2,wantedComp3,wantedDept1,
    wantedDept2,wantedDept3,wantedDept4,wantedDept5,wantedDept6,wantedDept7,
    wantedDept8,wantedDept9,wantedDept10,secondment,wantedLocation,restrictions,
    security,cohort):
        self.name = name
        self.priorDepartment = priorDepartment
        self.priorAnchor = priorAnchor
        self.priorSkill1 = priorSkill1
        self.priorSkill2 = priorSkill2
        self.priorLocation = priorLocation
        self.XX = XX
        self.wantedAnchor = wantedAnchor
        self.wantedSkill1 = wantedSkill1
        self.wantedAnchor2 = wantedAnchor2
        self.wantedSkill2 = wantedSkill2
        self.wantedComp1 = wantedComp1
        self.wantedComp2 = wantedComp2
        self.wantedComp3 = wantedComp3
        self.wantedDept1 = wantedDept1
        self.wantedDept2 = wantedDept2
        self.wantedDept3 = wantedDept3
        self.wantedDept4 = wantedDept4
        self.wantedDept5 = wantedDept5
        self.wantedDept6 = wantedDept6
        self.wantedDept7 = wantedDept7
        self.wantedDept8 = wantedDept8
        self.wantedDept9 = wantedDept9
        self.wantedDept10 = wantedDept10
        self.secondment = secondment
        self.wantedLocation = wantedLocation
        self.restrictions = restrictions
        self.security = security
        self.cohort = cohort



class Posting(object):

    def __init__(self, code, department, anchor, skill1, skill2, location, name,
    competency1, competency2, competency3, security, cohort):
        self.code = code
        self.department = department
        self.anchor = anchor
        self.skill1 = skill1
        self.skill2 = skill2
        self.location = location
        self.name = name
        self.competency1 = competency1
        self.competency2 = competency2
        self.competency3 = competency3
        self.security = security
        self.cohort = cohort

class Weighting(object):

    def __init__(self,department,anchor,skill,location,competency,restriction,
    previous_location):
        self.department = department
        self.anchor = anchor
        self.skill = skill
        self.location = location
        self.competency = competency
        self.previous_location = previous_location

class ReturnValue(object):
  def __init__(self, y0, y1, y2):
     self.y0 = y0
     self.y1 = y1
     self.y2 = y2
