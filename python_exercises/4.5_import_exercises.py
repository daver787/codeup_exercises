#Exercise 1
import function_exercises as fe
from function_exercises import cumsum
from function_exercises import remove_vowels as rv

fe.normalize_name('David')

#Exercise 2
import itertools as it
l1=list(it.product(('abc','123'),2)
l2=list(it.product(('abcd', '123'),2)
print(len(l1))
print(len(l2))
#Exercise 3
import json
import re
from collections import defaultdict, Counter
with open("profiles.json", "r") as read_file:
    profiles = json.load(read_file)
summary_dict = defaultdict(int)
fruits = []
messages = []
for profile in profiles:
    summary_dict['total_users'] += 1  #total number of users counter
    if profile['isActive'] == 'true':
        summary_dict['active_count'] += 1  #active users counter
    else:
        summary_dict['inactive_count'] += 1  #inactive users counter
    summary_dict['grand_total'] = summary_dict['grand_total'] + float(
        profile['balance'][1:].replace(",", ""))  #grand total accumulator
    fruits.append(profile['favoriteFruit'])
    messages.append(profile['greeting'])
summary_dict["average_balance"] = summary_dict["grand_total"] / summary_dict[
    "total_users"]  #average balance per user

#Count the fruits in fruit list with Counter or in dictionary
fruit_dict={}
for profile in profiles:
    print([fruit for fruit in profile['favoriteFruit']])


for fruit in fruits:
    if fruit in fruit_dict:
        fruit_dict['fruit']+=1
    else:
        fruit_dict['fruit']=1
print(fruit_dict)            
print(fruits)

counter = Counter(fruits)
print(counter)

#total number of unread messages
sum = 0
for message in messages:
    r1 = re.findall(r'\d+', message)
    sum = sum + int(r1[0])
print('The total number of unread messages is ' + str(sum) + '.')

#balance per user
d = defaultdict(list)
for profile in profiles:
    d[profile['balance']].append(profile['_id'])

print(d[sorted(d)[0]])
print(d[sorted(d, reverse=True)[0]])
