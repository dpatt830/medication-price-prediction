from bs4 import BeautifulSoup
import requests
import pandas as pd

# initializing an lists to store drug info
drug_info = []
drug_prices = []

# initializing a list to store hrefs
href_list = []

# establishing the url, requests page, and html parser object
# looking at the top 50 most commonly prescribed drugs; scraping price info
url = f"https://clincalc.com/DrugStats/Top300Drugs.aspx"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# looking at the text box which inlcudes names of the drugs
tr_tags = doc.find_all('tr')[:51]

# scraping the content in the td tags, creating a list that has the rank, price, and total prescriptions of the drug
# list example: ['drug rank', 'Name', 'total prescriptions']
for items in tr_tags:
    tds = items.find_all('td')

    # list will include additional info we do not need so only keep first 3 items
    td_texts = [td.text for td in tds]
    td_texts = td_texts[:3]
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

for href in href_list:

    # appending to our main drug list, a list of drug details
    drug_prices.append(cost(href))

# creating a dataframe from our td_text list
# we will later add onto the dataframe
df = pd.DataFrame(drug_info, columns=['Drug Rank', 'Drug Name', 'Total Prescriptions'])

# since csv has 51 rows, the 1st is an empty one but will fix that later
# adding in a random integer to the drug price list so lengths match
drug_prices.insert(0,1)

# adding the drug price list to the df
df['Average Drug Price Per Prescription'] = drug_prices

# creating a csv of our df
df.to_csv('Drug_Information.csv')