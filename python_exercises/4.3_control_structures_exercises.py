#Exercise 1a
day_of_week=input("Enter a day of the week")
if day_of_week=='Monday':
    print("Sorry not Monday")
else:
    print("It's Monday!")    
#Exercise 1b
weekend_or_not=input("Enter a day of the week")
if weekend_or_not in ['Saturday','Sunday']:
    print("It's the weekend!,Let's party") 
else:
     print("Sorry it's a workday") 
# Exercise 1c
num_hours=50
hour_wage=11

if num_hours<40:
    paycheck=num_hours*hour_wage
    print(paycheck)
else:
    paycheck=(num_hours-40)*1.5*hour_wage+40*hour_wage
    print("The weeks paycheck will be: "+str(paycheck))
 #Exercise 2a.1
i=5
while i<=15:
    print(i)
    i+=1  

#Exercise 2a.2
for i in range(0,102,2):
    print(i)

#Exercise 2a.3
for i in range(100,-10,-5):
    print(i)  

#Exercise 2a.4
i=2
while i**2<1000000:
    i=i**2
    print(i)

#Exercise 2a.5
for i in range(100,0,-5):
    print(i)

#Exercise 2b.1
num=input("Enter a number") 
num=int(num)
for i in range(1,11):
    print(str(i)+"*"+str(num)+"="+str(i*num)) 

#Exercise 2b.2
for num in range(1,9):
    print(str(num)*num)

#Exercise 2c.1 

odd_num=""
while True:
    odd_num=input("Enter an odd number between 1 and 50")
    if odd_num.isdigit() and int(odd_num)%2==1 and int(odd_num)>1 and int(odd_num)<50:
        break

for i in range(1,50,2):
    if i==int(odd_num):
        print("Yikes! Skipping number: "+str(i))
        continue
    print("Here is an odd number: "+str(i))
# Exercise 2d.1
pos_num=""

while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break

for i in range(1,int(pos_num+1)):
    print(i)

#Exercise 2e.1
pos_num=""
while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break
for i in range(int(pos_num),0,-1):
    print(i)

#Exercise 3
for i in range (1,101):
     if i%3==0 and i%5==0:
         print("FizzBuzz")
     elif i%3==0:
         print("Fizz")
     elif i%5==0:
         print("Buzz")
     else:
         print(str(i))
#Exercise 4
                                              

#Exercise 5
while True:
    num_grade=input("Please enter a grade between 0 and 100")
    num_grade=int(num_grade)
    if num_grade>=88:
        print('A')
    elif num_grade>=80:
        print('B')
    elif num_grade>=67:
        print('C')
    elif num_grade>=60:
        print('D') 
    else:
        print('F')
    prompt_user_continue=input("Would you like to continue? Y/N") 
    if prompt_user_continue.upper()=="N":
        break

#Exercise 6
book_list=[{'title':"Lamb",'author':"Christopher Moore",'genre':"fiction"},
{'title':"The Lean Startup",'author':"Eric Ries",'genre':"business"},{'title':"Devil in a White City",'author':"Eric Larson",'genre':"True Crime"},{'title':"Tom Sawyer",'author':"Mark Twain",'genre':"fiction"}]
for book in book_list:
    print("The book title is: "+book['title'])
    print("The book author is: "+book['author'])
    print("The book genre is: "+book['genre'])


#Exercise 6.a
genre_filter=input("Please enter a genre")
for book in book_list:
    if book['genre']==genre_filter:
        print("The book title is: "+book['title'])
        print("The book author is: "+book['author'])
    
