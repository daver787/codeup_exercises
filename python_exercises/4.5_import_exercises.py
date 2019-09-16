#Exercise 1
import function_exercises as fe
from function_exercises import cumsum
from function_exercises import remove_vowels as rv

fe.normalize_name('David')

#Exercise 2
import itertools
combinations(('abcd','123'))
combinations('abcd',2)

#Exercise 3
import json
import re
from collections import defaultdict,Counter
with open("profiles.json", "r") as read_file:
    data = json.load(read_file)
summary_dict=defaultdict(int)
fruit_list=[]
unread_messages=[]
for dict in data:
    summary_dict['total_users']+=1#total number of users counter
    if dict['isActive']=='true':
        summary_dict['active_count']+=1#active users counter
    else:
        summary_dict['inactive_count']+=1#inactive users counter
    summary_dict['grand_total']=summary_dict['grand_total']+float(dict['balance'][1:].replace(",",""))#grand total accumulator
    fruit_list.append(dict['favoriteFruit'])
    unread_messages.append(dict['greeting'])
summary_dict["average_balance"]=summary_dict["grand_total"]/summary_dict["total_users"]#average balance per user    
counter=Counter(fruit_list)
print(counter) 

sum=0 
for message in unread_messages:
    r1=re.findall(r'\d+',message)
    sum=sum+int(r1[0])  

#example below is in the docs.
d = defaultdict(list)
for dict in data:
    d[dict['balance']].append(dict['_id'])
