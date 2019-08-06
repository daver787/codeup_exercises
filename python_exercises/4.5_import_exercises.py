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
with open("profiles.json", "r") as read_file:
    data = json.load(read_file)
summary_dict={}    
for dic in data:
    if dic['isActive']=='True':
        summary_dict['active_count'] +=1
    else:
        summary_dict['inactive_count']+=1



