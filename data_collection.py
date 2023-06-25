from bs4 import BeautifulSoup
import requests
import pandas as pd

# initializing an lists to store drug info
drug_info = []
drug_prices = []
drug_class_date = []

# initializing a list to store hrefs
href_list = []

# establishing the url, requests page, and html parser object
# looking at the top 200 most commonly prescribed drugs; scraping price info
url = f"https://clincalc.com/DrugStats/Top300Drugs.aspx"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# looking at the text box which inlcudes names of the drugs
tr_tags = doc.find_all('tr')[:201]

# scraping the content in the td tags, creating a list that has the rank, price, and total prescriptions of the drug
# list example: ['drug rank', 'Name', 'total prescriptions']
for items in tr_tags:
    tds = items.find_all('td')

    # list will include additional info we do not need so only keep first 4 items
    td_texts = [td.text for td in tds]
    td_texts = td_texts[:4]

    # adding this info to the list
    drug_info.append(td_texts)

    # going through each a tag to get the href
    a_tags = items.find_all('a')
    for a_tag in a_tags:
       
        # finding the hrefs of each drug to search for individual drug info later on
        href = a_tag['href']

        # appending hrefs to list
        href_list.append(href)

def cost(href):
    # Function to scrape average costs of specific drugs given their href

    # establishing the url, requests page, and html parser object
    url = f'https://clincalc.com/DrugStats/{href}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    # finding at the chart displaying the different costs of the drug over the years
    # All the prices will be contained in this parent tag
    tr_tag = doc.find_all('tr')[5]

    tds = tr_tag.find_all('td')

    # Intializing price variable
    price = None

    # iterating through the td texts in tds
    for i in tds:

        # If it is the price, our price variable's value is that
        if '$' in i.text:
            price = i.text

            # removing the dollar sign to make the price a float variable
            price = float(price[1:])
            break
    return price

# now we will scrape each Established Pharmacologic Class (EPC)
# type/function of medication
# and the date it was approved byu the FDA
def EPC_and_date(href):
    # creating an empty list to store drug classification
    info = []

    # establishing the url, requests page, and html parser object
    url = f'https://clincalc.com/DrugStats/{href}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

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
    
    
    return epc_date

    


for href in href_list:

    # appending to our main drug list, a list of drug details
    drug_prices.append(cost(href))

    # using the EPC function to add drug classes for each drug
    drug_class_date.append(EPC_and_date(href)) 

# creating a dataframe from our td_text list
# we will later add onto the dataframe
df = pd.DataFrame(drug_info, columns=['Drug Rank', 'Drug Name', 'Total Prescriptions', 'Total Patients'])


# since csv has 51 rows, the 1st is an empty one but will fix that later
# adding in a random integer to the drug price list so lengths match
drug_prices.insert(0,1)

# Since the class and date list is a list of lists, have to insert a list
# at the first index to increse the row count
drug_class_date.insert(0,[1,1])

# adding the drug price list to the df
df['Average Drug Price Per Prescription'] = drug_prices

# adding the drug classes list to the df as well
epc_column = [item[0] for item in drug_class_date]
date_column = [item[1] for item in drug_class_date]
df['Drug Class'] = epc_column
df["FDA Approval Date"] = date_column

# creating a csv of our df
df.to_csv('Drug_Information.csv')