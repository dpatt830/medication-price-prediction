# Medication Price Data Analysis and Modeling: Overview (Ongoing)
* Creating a tool to observe the realtionship of multiple predictors on the effect of medication.
* Web scraped data regarding the 200 most widely prescribed drugs in the USA.
* Visualizing trends in the medications. 
* (Ongoing) Testing a linear model to show the relationship of the predictors and its effects on cost.

## Web Scraping
Utilized **BeautifulSoup** package in **Python** to scrape 200 entries of medication data, from (https://clincalc.com/DrugStats/Top200Drugs.aspx), to produce the following variables:
*	Drug Name
*	Total Prescriptions
*	Total Patients
*	Average Drug Price Per Prescription
*	Drug Class 
*	FDA Approval Date

## Data Cleaning
After the data was scraped, I needed to produce a way to visualize and parse the data collected:
* Created csv file to contain data
* Reformatted numeric variables to numeric types
* Integrated new column for generalized classification of medication
* Integrated new column for time medication has been on the market
