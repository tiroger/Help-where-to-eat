# %%
import sys

# %%
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
# %% markdown
# # Part 1: Data Extraction, aka: web scraping
# %%
michelin_rest = []

# 2. Enter Url
url = 'https://secretnyc.co/2019-michelin-star-restaurants-new-york-city/'
browser.visit(url)

html = browser.html

soup = BeautifulSoup(html, 'html.parser')
results = soup.find_all('a', target="_blank")

print(results)
all_names = []
for i in results:
    all_names.append(i.text)
print(all_names)
michelin_rest_name = all_names[1:-7]
michelin_rest_name

all_websites = []
for item in results:
    website = item.get('href')
    all_websites.append(website)
print(all_websites)

rest_website = all_websites[1:-7]
rest_website
nyc_michelin_restaurant_2019 = pd.DataFrame({'restaurant_name': michelin_rest_name, 'rest_website':rest_website, 'michelin_rated': True})
nyc_michelin_restaurant_2019.head()

nyc_michelin_restaurant_2019.to_csv('Resources/nyc_michelin_restaurant_2019.csv')
