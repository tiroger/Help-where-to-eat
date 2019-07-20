import pandas as pd
import numpy as np

import json
import requests
from config import google_api_key

import warnings
warnings.filterwarnings('ignore')


restaurant_2019_address = pd.read_csv('Final_Tables/restaurant_2019_address.csv')
restaurant_2019_address.head()
missing_address = restaurant_2019_address[restaurant_2019_address['street_address'].isna() == True]
missing_address.head()

url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'

name = missing_address['restaurant_name']

full_addresses = [] # Getting full address based on coordinates


for name in name:
    query_url = f'{url}input={name}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={google_api_key}'

    try:
        resp = requests.get(query_url)
        data = resp.json()
        print(data)
    except:
        print('Incorrectly formatted URL') # Accounts for NaN values in 'LOCATION'

    try:
        full_addresses.append(data['candidates'][0]['formatted_address'])
    except:
        print("No Data found") # Accounts for addresses not found in the Google API
        full_addresses.append('NaN')

full_addresses


missing_address['street_address'] = full_addresses
missing_address.head()

missing_address.to_csv('Resources/missing_address.csv')
