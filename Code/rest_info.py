# Importing dependecencies
import pandas as pd
import numpy as np
import datetime as datetime

# Opening and reading restaurant inspection dataset
rest_inspect = pd.read_csv('Resources/DOHMH_New_York_City_Restaurant_Inspection_Results.csv', encoding='utf-8', low_memory=False)
rest_inspect.head()
rest_inspect.columns
# For the restaurant info, we're interested in the following columns:
# - DBA: Name of establishment
# - BORO: self-explanatory
# - BUILDING: self-explanatory
# - STREET: self-explanatory
# - ZIPCODE: self-explanatory
# - PHONE: self-explanatory
# - CUISINE DESCRIPTION: self-explanatory
# - INSPECTION DATE: self-explanatory
# - CRITICAL FLAG: self-explanatory
# - SCORE: Restaurants with a score between 0 and 13 points earn an A, those with 14 to 27 points receive a B and those with 28 or more a C.
# - GRADE: Restaurant grade
# Other columns will be dropped

# Creating a copy of the dataframe including only the columns of interest
red_rest_inspect = rest_inspect[['DBA', 'BORO', 'BUILDING', 'STREET', 'ZIPCODE', 'PHONE', 'CUISINE DESCRIPTION', 'SCORE']].copy()
red_rest_inspect.head()

# Grouping data and aggregating for mean score
grouped_data = red_rest_inspect.groupby(['DBA', 'BORO', 'BUILDING', 'STREET', 'ZIPCODE', 'PHONE', 'CUISINE DESCRIPTION'])[['SCORE']].mean()
grouped_data.reset_index(inplace=True)
grouped_data.head()
len(grouped_data)

# Finding missing data and dropping rows with missing values
grouped_data.isna().sum()
grouped_data.dropna(inplace=True)
grouped_data.isna().sum()

# Renaming columns for clarity
renamed_inspect_2019 = grouped_data.rename(columns={'DBA': 'restaurant_name', 'BORO': 'borough', 'BUILDING': 'building_num', 'STREET': 'street', 'PHONE': 'phone_num', 'ZIPCODE': 'zip_code', 'CUISINE DESCRIPTION': 'cuisine', 'SCORE': 'score'})
renamed_inspect_2019.head()

# Adding grade column based on average score
renamed_inspect_2019['grade'] = 'B'
renamed_inspect_2019.loc[renamed_inspect_2019['score'] < 14,'grade'] = 'A'
renamed_inspect_2019.loc[renamed_inspect_2019['score'] > 27,'grade'] = 'C'
renamed_inspect_2019.head()

# Formatting phone numbers and zip codes
formatted_numbers = []
for phone_no in renamed_inspect_2019['phone_num']:
    contactphone = "(%c%c%c)%c%c%c-%c%c%c%c" % tuple(map(ord,list(str(phone_no)[:10])))
    formatted_numbers.append(contactphone)
renamed_inspect_2019['phone_num'] = formatted_numbers
formatted_zips = renamed_inspect_2019['zip_code'].astype('int64')
renamed_inspect_2019['zip_code'] = formatted_zips
renamed_inspect_2019.head()

# Formatting restaurant names to match case
renamed_inspect_2019['restaurant_name'] = renamed_inspect_2019['restaurant_name'].str.lower()
renamed_inspect_2019['restaurant_name'] = renamed_inspect_2019['restaurant_name'].str.title()

# Formatting borough to match case
renamed_inspect_2019['borough'] = renamed_inspect_2019['borough'].str.lower()
renamed_inspect_2019['borough'] = renamed_inspect_2019['borough'].str.title()

renamed_inspect_2019.isna().sum()

# Creating and saving tables for database
restaurant_info = renamed_inspect_2019[['restaurant_name', 'borough', 'building_num', 'street', 'zip_code', 'phone_num']]
restaurant_info.set_index('restaurant_name', inplace=True)
restaurant_info.head()
restaurant_info.to_csv('Tables/restaurant_info.csv', encoding='UTF-8')

restaurant_score = renamed_inspect_2019[['restaurant_name', 'score', 'grade']]
restaurant_score.set_index('restaurant_name', inplace=True)
restaurant_score.head()
restaurant_score.to_csv('Tables/restaurant_score.csv', encoding='UTF-8')

restaurant_cuisine = renamed_inspect_2019[['restaurant_name', 'cuisine']]
restaurant_cuisine.set_index('restaurant_name', inplace=True)
restaurant_cuisine.head()
restaurant_cuisine.to_csv('Tables/restaurant_cuisine.csv', encoding='UTF-8')

# Opening and reading restaurant week 2018 dataset
rest_week_2018 = pd.read_csv('Resources/restaurant_week_2018_final.csv', encoding='utf-8')
rest_week_2018.head()

rest_week_2018.columns

# creating a new datafrane with restaurant website
rest_website = rest_week_2018[['name', 'website']].copy()
rest_website.head()
