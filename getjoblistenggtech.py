
import requests,time
import json

resp_skillsfilter = requests.get("http://api.dataatwork.org/v1/skills/autocomplete?contains=\"engineering and technology\"")
data_skillsfilter = resp_skillsfilter.text
dict_skillsfilter = json.loads(data_skillsfilter)
#print(len(r_skillsfilter[0]))
print(json.dumps(dict_skillsfilter,indent=4))

arry_joblist = []
arry_joblist.clear()

#Begin FOR Loop for getting the job list for specific "uuid"s related to
# 'engineering and technology'
for i in dict_skillsfilter:
    #print(i)
    skill_uuid_engg_tech = i['uuid']
    #UUID for 'engineering and technology'
    print("UUID for 'engineering and technology': " + skill_uuid_engg_tech)

    resp_joblist = requests.get("http://api.dataatwork.org/v1/skills/" + skill_uuid_engg_tech + "/related_jobs")
    data_joblist = resp_joblist.text
    dict_joblist=json.loads(data_joblist)
   #print(json.dumps(dict_joblist, indent=4))
    print("Number of Jobs posted :", len(dict_joblist['jobs']))

    print("--------------------")
    print(" List of Job Titles ")
    print("--------------------")

    #Store the job list in the array
    for i in dict_joblist['jobs']:
        arry_joblist.append(i['job_title'])

#End of For Loop

# Print the array Joblist with the number of records
print(len(arry_joblist))
print(arry_joblist)
headers={"Title": "Engineering Jobs"}
data=json.dumps(arry_joblist)

#Post the array data to requestbin
rd = requests.post('https://en4832wfm1s7a.x.pipedream.net', headers=headers, data=data)
print(rd.text)