from bs4 import BeautifulSoup
import requests
import pandas as pd
import re 
# Function to scrape costs of specific drugs given their href
# over the timeline of 2013 - 2020
#href = 'Drugs/Atorvastatin'

# establishing the url, requests page, and html parser object
url = f'https://clincalc.com/DrugStats/Drugs/Buspirone'
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# creating an empty list to store drug classification
info = []

# findint teh table in which the classification is held in 
# finding the table in which the info is held in 
table_tags = doc.find_all('table')[-1]

# Now sifting through teh td tags in that table
td_tags = table_tags.find_all('td')

# appending all text td tags in the list
for i in td_tags:
    info.append(i.text)

epc_date = info[1:2] + info[3:4]

# some drug EPC is N/A so we will mark it as N/A if missing
if epc_date[0] == None:
    epc_date[0] = 'N/A'


    


# Intializing price variable

'''
    for tr_tags in tr_tag:
        num_of_prescriptions = tr_tag[1].find('td')[1].text
        print(num_of_prescriptions)
'''
'''
numbers = re.findall(r"[-+]?\d*\.\d+|\d+", script)

for i in numbers:
    print(i)
'''