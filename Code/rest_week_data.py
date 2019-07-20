import numpy as np
import pandas as pd

# Opening and reading datasets
rest_inspect = pd.read_csv('Resources/cleaned_restaurant_inspection_data.csv')
rest_inspect.head()

rest_week_2019 = pd.read_csv('Resources/restaurant_week_2019_final.csv')
rest_week_2019.head()

#Renaming columns
rest_week_2019.rename(columns={'Restaurant': 'restaurant_name', 'Location': 'location', 'Ratings': 'rating', 'Cuisine': 'cuisine', 'Specials': 'specials'}, inplace=True)
rest_week_2019.head()
# Checking for duplicates
rest_week_2019.duplicated().sum()
rest_inspect.duplicated().sum()

rest_week_2018 = pd.read_csv('Resources/restaurant_week_2018_final.csv')
rest_week_2018.head()


rest_week_2018.rename(columns={'name': 'restaurant_name'}, inplace=True)
rest_week_2018.head()

# Merging datasets
merged_rest_week_2019 = pd.merge(rest_week_2019, rest_week_2018, how='left', on='restaurant_name')
merged_rest_week_2019.head()

len(merged_rest_week_2019)

# Dropping extraneous columns
#merged_rest_week_2019.drop(columns={'Unnamed: 0'}, inplace=True)
merged_rest_week_2019.head()

# Merging with restaurant inspection dataframe

complete_rest_week_2019 = pd.merge(merged_rest_week_2019, rest_inspect, how='left', on='restaurant_name')
complete_rest_week_2019.head()

complete_rest_week_2019.columns
# Cleaning up final Table
final_restaurant_week_table = complete_rest_week_2019[['restaurant_name', 'location', 'rating', 'cuisine', 'specials',
       'street_address', 'google_map', 'review_count', 'phone', 'website',
       'restaurant_type', 'average_review', 'food_review', 'service_review',
       'ambience_review', 'value_review', 'price_range', 'star_1', 'star_2',
       'star_3', 'star_4', 'star_5', 'inspection_score',
       'grade']]
final_restaurant_week_table.set_index('restaurant_name', inplace=True)
final_restaurant_week_table.head()
final_restaurant_week_table.isna().sum()

# Creating seperate tables for database
#----
#1. Restaurant Cuisine
restaurant_2019_cuisine = final_restaurant_week_table[['cuisine']]
restaurant_2019_cuisine.head()
restaurant_2019_cuisine.to_csv('Final_Tables/restaurant_2019_cuisine.csv')
#---
#2. Open Table Reviews
open_table_review = final_restaurant_week_table[['rating']]
open_table_review.head()
open_table_review[open_table_review['rating'].isna()]
# Manually filling in missing values
open_table_review.loc['Benjamin Steakhouse Prime']['rating'] = '92% Recommend'
open_table_review.loc['Lorenzo\'s Restaurant, Bar & Caberet - Hilton Garden Inn - SI']['rating'] = '88% Recommend'
open_table_review.loc['Junoon Main Dining Room']['rating'] = '33% Recommend'
open_table_review[open_table_review['rating'].isna()]
# Renaming table to be more descriptive
open_table_review.rename(columns={'rating': 'open_table_recommend'}, inplace=True)
open_table_review.head()
open_table_review[['num', 'perc']] = open_table_review['open_table_recommend'].str.split(' ', expand=True)
open_table_review.head()
open_table_review['num'] = open_table_review['num'].str.replace('%', '')
open_table_review.head()
open_table_review.drop(['open_table_recommend', 'perc'], axis=1, inplace=True)
restaurant_2019_open_table_review = open_table_review.rename(columns={'num': 'percent_recommend'})
restaurant_2019_open_table_review.head()
restaurant_2019_open_table_review.to_csv('Final_Tables/restaurant_2019_open_table_recommend.csv')

#----
#3. Restaurant neighborhood
restaurant_2019_neighborhood = final_restaurant_week_table[['location']]
restaurant_2019_neighborhood.head()
restaurant_2019_neighborhood.rename(columns={'location': 'neighborhood'}, inplace=True)
restaurant_2019_neighborhood.isna().sum()
restaurant_2019_neighborhood.to_csv('Final_Tables/restaurant_2019_neighborhood.csv')
#---
#4. Restaurant address
# see Combine_address_data file
#---
# 5. Yelp Scores
restaurant_2019_yelp_review = final_restaurant_week_table[['average_review', 'food_review', 'service_review', 'ambience_review', 'value_review']]
restaurant_2019_yelp_review.head()
restaurant_2019_yelp_review.to_csv('Final_Tables/restaurant_2019_yelp_review.csv')

#---
# 6. Inspection grades

restaurant_2019_inspec_grade = final_restaurant_week_table[['inspection_score','grade']]
restaurant_2019_inspec_grade.head()
restaurant_2019_inspec_grade.isna().sum()
restaurant_2019_inspec_grade.to_csv('Final_Tables/restaurant_2019_inspec_grade.csv')
#---
