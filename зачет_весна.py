import json
import os
from collections import Counter
import matplotlib.pyplot as plt
# def read_json_files(path):
#     new_file = []
#     for folder in os.listdir(path):
#         for file in os.listdir(f"{path}/{folder}"):
#             if file.endswith(".json"):
#                 with open(f"{path}/{folder}/{file}",'r') as json_file:
#                     data=json.load(json_file)
#                     if data not in new_file:
#                         new_file.append(data)
#     return new_file
#
#
# path=r'C:\Users\irish\PycharmProjects\pythonlessons\Новая папка\main folder'
# new_file = read_json_files(path)
# with open('new_directory/new_file.json','w') as json_file:
#     json.dump(new_file, json_file, indent=2)


with open(r'C:\Users\irish\PycharmProjects\pythonlessons\new_directory\new_file.json', 'r') as json_file:
    data=json.load(json_file)
list_of_skills=[]
for item in data:
    list_of_skills.extend(item['skills'])
# print(list_of_skills)
skills_count=Counter(list_of_skills)
print(skills_count)

with open('counter.json', 'w') as json_file:
    json.dump(skills_count,json_file, indent=2)


# for skill, count in skills_count.items():
#     print(f'{skill}:{count}')

x=list(skills_count.keys())
y=list(skills_count.values())
plt.barh(x,y)
plt.show()