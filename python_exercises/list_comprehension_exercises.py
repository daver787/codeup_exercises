# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits=[fruit.upper() for fruit in fruits]
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
uppercased_fruits_2=[fruit[0].upper()+fruit[1:] for fruit in fruits]
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
vowel_list=["a","e","i","o","u"]
counter=0
fruits_with_more_than_two_vowels=[]
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels=[fruit for fruit in fruits if fruit.count('aeiou')>2]
# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_five_char_fruits=[fruit for fruit in fruits if len(fruit)>5]
# Exercise 6 - make a list that contains each fruit with exactly 5 characters
five_char_fruits=[fruit for fruit in fruits if len(fruit)=5]
# Exercise 7 - Make a list that contains fruits that have less than 5 characters
less_five_char_fruits=[fruit for fruit in fruits if len(fruit)<5]
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
num_char_fruits=[len(fruit) for fruit in fruits]
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a=[fruit for fruit in fruits if 'a' in fruit]
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers=[number for number in numbers if number%2==0]
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers=[number for number in numbers if number%2==1]
# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers=[number for number in numbers if number>0]
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers=[number for number in numbers if number<0]
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
more_numerals=[number for number in numbers if len(str(abs(number)))>=2]
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared=[number**2 for number in numbers]
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers=[number for number in numbers if (number%2==1 and number<0)] 
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_five=[number+5 for number in numbers]
# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.


#Exercise 3 and 4 without list comprehension
test=[]
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
vowels=["a","e","i","o","u"]
for fruit in fruits:
    counter=0
    for vowel in vowels:
        num_vowels=fruit.count(vowel)
        counter=counter+num_vowels
    #if counter==2:
    if counter>2:    
        test.append(fruit)    

