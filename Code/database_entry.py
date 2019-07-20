import pandas as pd
from sqlalchemy import create_engine

rds_connection_string = "postgres:postgres@localhost:5432/restaurant_week_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

engine.table_names()

# Opening dataframes
restaurant_2019_address = pd.read_csv('Final_Tables/restaurant_2019_address.csv')
restaurant_2019_cuisine = pd.read_csv('Final_Tables/restaurant_2019_cuisine.csv')
restaurant_2019_inspec_grade = pd.read_csv('Final_Tables/restaurant_2019_inspec_grade.csv')
restaurant_2019_neighborhood = pd.read_csv('Final_Tables/restaurant_2019_neighborhood.csv')
restaurant_2019_open_table_recommend = pd.read_csv('Final_Tables/restaurant_2019_open_table_recommend.csv')
restaurant_2019_yelp_review = pd.read_csv('Final_Tables/restaurant_2019_yelp_review.csv')

restaurant_2019_address.to_sql(name='restaurant_address', con=engine, if_exists='append', index=False)
restaurant_2019_cuisine.to_sql(name='restaurant_cuisine', con=engine, if_exists='append', index=False)
restaurant_2019_inspec_grade.to_sql(name='restaurant_inspection_results', con=engine, if_exists='append', index=False)
restaurant_2019_neighborhood.to_sql(name='restaurant_neighborhood', con=engine, if_exists='append', index=False)
restaurant_2019_open_table_recommend.to_sql(name='restaurant_open_table_review', con=engine, if_exists='append', index=False)
restaurant_2019_yelp_review.to_sql(name='restaurant_yelp_review', con=engine, if_exists='append', index=False)
