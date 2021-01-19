import requests
import json


class Skills:
    def __init__(self, uuid, name, type, description, onet_element_id, normalized_skill_name):
        self.uuid = uuid
        self.name = name
        self.type = type
        self.description = description
        self.onet_element_id = onet_element_id
        self.normalized_skill_name = normalized_skill_name

    @classmethod

    def from_json(cls, skill_string):
        skills_dict = json.loads(skill_string)
        return cls(**skills_dict)

    def __repr__(self):
        return f'<User {self.name}>,'

#r_skills = requests.get("http://api.dataatwork.org/v1/skills").json()
responsejobs = requests.get("http://api.dataatwork.org/v1/jobs")
datajobs = responsejobs.text
print(type(datajobs))

r_jobs = json.loads(datajobs)
print(len(r_jobs[0]))
for i in r_jobs:
    print(i)

responseskills = requests.get("http://api.dataatwork.org/v1/skills")
dataskills = responseskills.text
print(type(dataskills))

r_skills = json.loads(dataskills)
print(len(r_skills[0]))
for i in r_skills:
    print(i)


responseskillsfilter = requests.get("http://api.dataatwork.org/v1/skills/autocomplete?contains=\"engineering and technology\"")
dataskillsfilter = responseskillsfilter.text
print(type(dataskillsfilter))

r_skillsfilter = json.loads(dataskillsfilter)
print(len(r_skillsfilter[0]))
for i in r_skillsfilter:
    print(i)
    skill_uuid_engg_tech = r_skillsfilter[0]['uuid']
    print(skill_uuid_engg_tech)


#responsesjoblist = requests.get("http://api.dataatwork.org/v1/skills/c09c8f8c163907ac25a37c3dd591ba2e/related_jobs")
responsesjoblist = requests.get("http://api.dataatwork.org/v1/skills/" + skill_uuid_engg_tech + "/related_jobs")
datajoblist = responsesjoblist.text
print(type(datajoblist))

r_joblist = json.loads(datajoblist)
print(len(r_joblist['jobs']))

#for i in r_joblist['jobs']:
#    print(i)

#for i in r_skills[]
#print(r_skills[0]['uuid'])

#print(json.dumps(r_skills, indent=4))
#print(r_skills)

#[print(key,value) for key, value in r_skills.uuid()]



#names = r_skills["name"]
#print(names)

#
#print(r_skills)
#skills = Skills.from_json(r_skills)
#print(skills)