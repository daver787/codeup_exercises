#Exercise 1
def istwo(num):
    if int(num)==2:
        return True
    else:
        return False 

#Exercise 2
def isvowel(character):
    if character in ['a','e','i','o','u']:
        return True
    else: 
        return False 

#Exercise 3
def is_consonant(char):
     if isvowel(char)==True:
         return False
     else:
         return True           
        
#Exercise 4
def captialize_consonant(word):
    if is_consonant(word[0])==True:
        return word[0].upper()+word[1:]
    else:
         return word

#Exercise 5
def calculate_tip(tip_percentage,bill):
    return(tip_percentage/100*bill)

#Exercise 6
def apply_discounts(original_price,discount_percentage):
    return original_price*(1-discount_percentage)

#Exercise 7
def handle_commas(number):
    return int(number.replace(",",""))

#Exercise 8
def get_letter_grade(num_grade):
    num_grade=int(num_grade)
    if num_grade>=88:
        return('A')
    elif num_grade>=80:
        return('B')
    elif num_grade>=67:
        return('C')
    elif num_grade>=60:
        return('D') 
    else:
        return('F')

#Exercise 9
def remove_vowels(word):
    for char in word:
        if char in ['a','e','i','o','u']:
            word=word.replace(char,"")
    return word 

#Exercise 10
def normalize_name(string):
    string=string.lstrip().rstrip().lower().replace(" ","_")
    counter=1
    while True:
        if string.isidentifier():
            break
        else:
            string=string[counter:] 
            counter +=1 
    return string

#Exercise 11
def cumsum(num_list):
    cumsum_list=[]
    for ele,num in enumerate(num_list):
        if ele==0:
            csum=num
        else:
            csum=csum+num_list[ele]
        cumsum_list.append(csum)
    return cumsum_list        

#Bonus1
def twelveto24(time):
    if time[-2:-1]=="am":
        position=time.index(:)
        twenty_four=int(time[:position])+12
        time=str(twenty_four)+time[position+1:-2]
    else:
        time=time[:-2] 
    return time     









#Bonus2












            