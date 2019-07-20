import pandas as pd
import numpy as np
import re

restaurant_2019_address = pd.read_csv('Final_Tables/restaurant_2019_address.csv')
restaurant_2019_address.head()
restaurant_2019_address[restaurant_2019_address['street_address'].isna() == True]


# Extracting zip code from address column
restaurant_2019_address['zip_code'] = restaurant_2019_address['street_address'].str.extract('(\d{5})')
restaurant_2019_address['street_address'] = restaurant_2019_address['street_address'].str.replace('(\d{5})', '')
restaurant_2019_address.head()

nyc_zip = pd.read_csv('Resources/zip_borough.csv')
nyc_zip.head()
nyc_zip.rename(columns={'zip': 'zip_code'}, inplace=True)
nyc_zip.head()
nyc_zip.dtypes

# Converting restaurant_2019_address to int





mod_restaurant_2019_address = pd.merge(restaurant_2019_address, nyc_zip, on='zip_code', how='left')




restaurant_2019_address.to_csv('Resources/mod_restaurant_2019_address.csv')
