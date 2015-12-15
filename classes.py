class Candidate:

    def __init__(self, name, departments, anchor, skills, security):
        self.name = name
        self.departments = departments
        self.anchor = anchor
        self.skills = skills
        self.security = security

Jamie = ["Jamie", 'HMRC', 'Operational', 'Delivery, Digital', 'CTC']
Jonathan = ["Jonathan", 'DWP', 'Operational', 'Delivery', 'CTC']
candidate = [Candidate(*Jamie),
             Candidate(*Jamie)]

#print(candidate[0].skills)
#print(candidate[1].name)

class Posting:

    def __init__(self, code, department, anchor, skill1, skill2, location, name,
    competency1, competency2, competency3, security):
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
