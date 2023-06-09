from bs4 import BeautifulSoup
import requests
import pandas as pd

# initializing an overall list to store drug info
drugs = []

# initializing a list to store hrefs
href_list = []

# establishing the url, requests page, and html parser object
# looking at the top 50 most prescribed drugs in 2020; scraping price info
url = f"https://clincalc.com/DrugStats/Top300Drugs.aspx"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# looking at the text box which inlcudes names of the drugs
tr_tags = doc.find_all('tr')[:51]

# scraping each drugs' name and href
for items in tr_tags:
    a_tags = items.find_all('a')
    for a_tag in a_tags:
        name = a_tag.text
        href = a_tag['href']
        href_list.append(href)

def cost_timeline(href):
    # Function to scrape costs of specific drugs given their href
    # over the timeline of 2013 - 2020

    # establishing the url, requests page, and html parser object
    url = f'https://clincalc.com/DrugStats/{href}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    # finding at the chart displaying the different costs of the drug over the years
    # All the prices will be contained in this parent tag
    div = doc.find_all('div', id="divPrescriptionCostOverTime")

    # iterating each subsequent tag
    for items in div:

        # locating specifically 'tr' tags which contain the price strings
        tr_tags = items.find_all('tr')[1:]
        print(tr_tags)
print(tr_tags)