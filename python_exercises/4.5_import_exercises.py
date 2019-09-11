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
from collections import defaultdict
with open("profiles.json", "r") as read_file:
    data = json.load(read_file)
summary_dict=defaultdict(int) 
for dict in data:
    summary_dict['total_users']+=1#total number of users counter
    if dict['isActive']=='true':
        summary_dict['active_count']+=1#active users counter
    else:
        summary_dict['inactive_count']+=1#inactive users counter

    summary_dict['grand_total']=summary_dict['grand_total']+float(dict['balance'][1:].replace(",",""))#grand total accumulator
    summary_dict["average_balance"]=summary_dict["grand_total"]/summary_dict["total_users"]#average balance per user
