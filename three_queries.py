# -*- coding: utf-8 -*-
"""Three Queries

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12jOCdBmR1eBluvOnmjGpIlWWlv5ET3aT
"""

#QUERY 1 - TOTAL JOBS ANALYZED

import pandas as pd

df = pd.read_csv('FinalJobDataUpdated.csv')

# Count the total number of rows in the dataframe -- Each row represents 1 job
num_rows = len(df)


print("Total Jobs Analyzed:", num_rows)

#Query, average salary of each search parameter "Data Analyst", "Data Engineer", "Data Scientist"


import pandas as pd

df = pd.read_csv('FinalJobDataUpdated.csv')

# Group by each unique value in the 'Search Parameter' column and take the group's average of the "Average Salary" column
grouped_df = df.groupby(['Search Parameter'])['Average Salary'].mean()


grouped_df = grouped_df.apply(lambda x: '${:,.2f}'.format(x))

print(grouped_df)

#Query, Top 5 highest paying cities

import pandas as pd

df = pd.read_csv('FinalJobDataUpdated.csv')

top_paying_cities = df.groupby(['City', 'State Code'])['Average Salary'].mean().sort_values(ascending = False)

print(top_paying_cities)