# merging our two csv's to get a final one

import pandas as pd

# reading in files and creating df's of our csv's
file = "C:\\Users\\Owner\\OneDrive - Loyola University Chicago\\Summer_Projects_2023\\medication-price-prediction\\Clean_Drug_Information.csv"

file2 = "C:\\Users\\Owner\\OneDrive - Loyola University Chicago\\Summer_Projects_2023\\medication-price-prediction\\Unique_Classes.csv"

df1 = pd.read_csv(file)

df2 = pd.read_csv(file2)

# merging our csv's
new_df = pd.merge(df1, df2, on='Drug Class', how='left')

''' Quick cleaning'''

# dropping useless columns
columns_drop = ['Unnamed: 9','General Classification_x','Drug Name_y']   

new_df = new_df.drop(columns=columns_drop)

# renaming new column
new_df = new_df.rename(columns={'General Classification_y': 'General Classification'})

# writing to csv file
new_df.to_csv("Complete_Drug_Info.csv")