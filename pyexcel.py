import pandas as pd
import numpy as np 
from openpyxl.workbook import Workbook
df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None) #telling py there is no header, otherwise 1st row will be used as header
df_txt = pd.read_csv('data.txt', delimiter ='\t') #makes text file readable by telling py to seperate by tab

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'zip', 'Income'] #creates header

#DATA VIEWING BASICS

#df_csv.to_excel('motified_Names.xlsx') #saves to new excel workbook
#print(df_csv['First'][0:3])# prints first 3 rows of First column
#print(df_csv.iloc[1]) #prints first row of all columns
#print(df_csv.loc[(df_csv['City'] == 'Riverside') & (df_csv['First'] == 'John')]) #prints all rows where city = Riverside and First is John

#creates tax bracket column based on income. 
#df_csv['Tax%'] = df_csv['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)
#df_csv['Taxes Owed'] = df_csv['Income'] * df_csv['Tax%']

#dropping unneeded columns
#to_drop = ['First', 'zip', 'Address']
#df_csv.drop(columns= to_drop, inplace=True) #inplace flag means the df of this instance. Dont need df = to itself 

#creating and column that chages values based on conditions of another column/s
#df_csv['Test Col'] = False
#df_csv.loc[df_csv['Income'] < 60000, 'Test Col'] = True

#finds avg of Test Column values, sorts by Income low ot high
#print(df_csv.groupby(['Test Col']).mean().sort_values('Income'))

#DATA CLEANING 
df_csv.drop(columns = 'Address', inplace=True)
df_csv = df_csv.set_index('zip') #sets zip as primary key, or index

df_csv.First = df_csv.First.str.split(expand=True) #splits string in First column. Cleans first names and removes middle and nicknames
df_csv = df_csv.replace(np.nan, 'N/A', regex=True) #replaces and NAN values in df with N/A

to_excel = df_csv.to_excel('motified_clean_data.xlsx')
