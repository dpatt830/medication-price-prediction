import pandas as pd

# initializing our csv file
file = "C:\\Users\\Owner\\OneDrive\\Desktop\\Summer_Projects_2023\\medication-price-prediction\\Drug_Information.csv"

# Creating our overall data frame
df = pd.read_csv(file)

''' General cleaning of the csv'''

# removing the first row
value = 1
df = df.drop(df[df['FDA Approval Date'] == value].index)


# converting the total prescrptions and total patients columns to integers
df['Total Prescriptions'] =  df['Total Prescriptions'].str.replace(',', '').astype(float)
df['Total Patients'] =  df['Total Patients'].str.replace(',', '').astype(float)

# creating a csv of our new cleaner df
df.to_csv('Clean_Drug_Information.csv')