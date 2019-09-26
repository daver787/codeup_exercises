""" 1)Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

Use pandas to create a Series from the following data:

["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
a)Name the variable that holds the series fruits.

b)Run .describe() on the series to see what describe returns for a series of strings.

c)Run the code necessary to produce only the unique fruit names.

d)Determine how many times each value occurs in the series.

e)Determine the most frequently occurring fruit name from the series.

f)Determine the least frequently occurring fruit name from the series.

g)Write the code to get the longest string from the fruits series.

h)Find the fruit(s) with 5 or more letters in the name.

i)Capitalize all the fruit strings in the series.

j)Count the letter "a" in all the fruits (use string vectorization)

k)Output the number of vowels in each and every fruit.

l)Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

m)Write the code to get only the fruits containing "berry" in the name

n)Write the code to get only the fruits containing "apple" in the name

o)Which fruit has the highest amount of vowels?
 """
import pandas as pd
import matplotlib.pyplot as plt

fruits=pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
#fruits.head()
#fruits.describe()
#print(fruits.unique())
#print(fruits.value_counts().nlargest(n=1))
#print(fruits.value_counts().nsmallest(n=1))
print(fruits[fruits.str.len().idxmax()])
#print(fruits.apply(len))

def length_of_fruits(fruit):
    return len(fruit)

""" 2) Use pandas to create a Series from the following data:
['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
What is the data type of the series?
Use series operations to convert the series to a numeric data type.
What is the maximum value? The minimum?
Bin the data into 4 equally sized intervals and show how many values fall into each bin.
Plot a histogram of the data. Be sure to include a title and axis labels. """

series1 = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
print('The data type of the series is: '+str(type(series1)))
series1 = series1.replace({'\$':'',',':''},regex=True).astype('float')
print(series1.max())
print(series1.min())
print(pd.cut(series1,4).value_counts())
series1.plot.hist()
plt.title('Histogram of salary values')
plt.xlabel('Bins')
plt.ylabel('Frequency')