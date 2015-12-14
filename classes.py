class Candidate:

    def __init__(self, name, departments, anchor, skills, security):
        self.name = name
        self.departments = departments
        self.anchor = anchor
        self.skills = skills
        self.security = security


candidate = [Candidate("Jamie", 'HMRC', 'Operational', 'Delivery, Digital', 'CTC'),
             Candidate("Jonathan", 'DWP', 'Operational', 'Delivery', 'CTC')]

print(candidate[0].skills)
print(candidate[1].name)

class Posting:

    def __init__(self, name, department,anchor,skills, security):
        self.name = name
        self.department = department
        self.anchor = anchor
        self.skills = skills
        self.security = security
