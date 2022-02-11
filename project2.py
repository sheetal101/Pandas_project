import pandas as pd
import json
from csv import reader
import matplotlib.pyplot as plt

# READING THE CSV FILE 

file_name='/home/dell31/Downloads/archive/28_Trial_of_violent_crimes_by_courts.csv'
df=pd.read_csv(file_name)
# print(df)

# 1. REMOVING DUPLICATE ROWS 

a=df.duplicated()
df.drop(df.index[a], inplace=True) 
# print(df)


# 2. REMOVING NULL,NAN VALUES WIHTOUT CHANGING THE INDEX

df.dropna(axis=0,inplace=True)
df.to_csv(file_name,index=False)
# print(df)


# 3. CHECK DATA TYPE

for i in df:
    for x in df[i]:
        # Below statement can show the type of value in each column
        print(type(x), x)


#4. READING CSV FILE FROM ROWS IT RETURNS LIST OF ROWS

with open('28_Trial_of_violent_crimes_by_courts.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)

#5. CREATING STATIC, ANIMATED VISUALIZATIONS
#  I AM TAKING  TOP 5 STATE'S NAME AND TOP 5 VIOLENT CRIME'S RECORDS TO MAKE BAR GRAF

col_1=df['Area_Name'].head(5)
col_2=df["Trial_of_Violent_Crimes_by_Courts_By_trial"].head(5)

plt.xlabel("Area_Name", fontsize=12)
plt.ylabel("Trial_of_Violent_Crimes_by_Courts_By_trial", fontsize=13)
plt.bar(col_1, col_2)
plt.show()    



    





