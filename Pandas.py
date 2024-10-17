what is Pandas ?
Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:
  #  reshaping
 # merging
 # sorting
 # slicing
 # aggregation
imputation. If you are using anaconda, you do not have install pandas.
for windows 
pip install conda
pip install pandas

Name
0 Abdulkadir
1 Yaasiin
2 Bilal
Countries Series
Country 
0 The Netherlands
1 Somalia
3 Kuwait 

City
0 The Hague
1 Mogadishu
3 Kuwait city 
Let us see, an example of a pandas data frame:
Name Country City
0 Abdulkadir The Netherlands The Hague
1 Yaasiin Somalia Mogadishu
2 Bilal  kuwait Kuwait city

Importing Pandas 

import pandas as pd
import numpy as np
# Creating Pandas Series with Default Index
nums = pd.Series([1, 2, 3, 4, 5])
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
# Creating Pandas Series from a Dictionary
dct ={'name':'Abdulkadir','country':'The Netherlands','city':'The Hague'}
s = pd.Series(dct)
print(s)

# Creating a Constant Pandas Series
s = pd.Series(5, index=[0, 1, 2, 3, 4])
print(s)

# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(1, 5, 5))
print(s)

# DataFrames

reating DataFrames from List of Lists
data = [
    ['Abdulkadir', 'The Netherlands', 'The Hague'], 
    ['Yaasiin', 'Somalia', 'Mogadishu'],
    ['Bilal', 'kuwait', 'Kuwait city']
    

]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary
data = {'Name': ['Abdulkadir', 'Yaasiin', 'Bilal'], 'Country':[
    'The Netherlands', 'Somalia', 'kuwait'], 'City': ['The Hague', 'Mogadishu', 'Kuwait city']}
df = pd.DataFrame(data)
print(df)

# Reading CSV File Using Pandas
curl -O https://raw.githubusercontent.com/Abdulkadir/Pandas.py/master/data/weight-height.csv

import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)

 #Creating a DataFrame
 import pandas as pd
 data = {
     'Name': ['Abdulkadir', 'Yaasiin', 'Bilal'], 
     'Country': ['The Netherlands', 'Somalia', 'kuwait'],
     'City': ['The Hague', 'Mogadishu', 'Kuwait city']
 }
 df = pd.DataFrame(data)
 print(df)






