# RESTAURANT WEEK 2019 - Project Report
Roger Lefort
Xiaoqi Wendy Guo

## Help! Where should I eat?
### Restaurant Week: July 22 - August 16, 2019

Our goal is that this resulting database can be used to quickly finding and visualizing information about NYC restaurants participating in Restaurant Week 2019 and help inform consumer's decision as to which restaurant to patron.

Through the project, we have performed a full ETL procedure on the data:

**Extract**: 
The database was created by combining the following data sources: 

- NYC restaurant inspection data: [Open data](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j), available as a csv file

- NYC Restaurant Week 2018 data: https://www.kaggle.com/popoandrew/restaurant-week-2018 , available as a csv file

- Open Table: obtained from scraping the restaurant week [page](https://www.opentable.com/promo.aspx?covers=2&currentview=list&datetime=2019-07-22+19%3A00&latitude=40.803606&longitude=-73.981648&metroid=8&promoid=69&ref=412&size=100&sort=Name)

The original data sources indicated above contains 2 csv files including restaurant inspection data and yelp reviews data. We also performed a scraping activity to extract the 2019 participated restaurant data from OpenTable website into a dataframe in pandas and extracted as a csv file.

**Transform**:

After reviewing the data, we determined that the following information for each restaurant will be helpful for consumers to make decisions:
- Restaurant Name
- Address and phone number
- Cuisine type
- Inspection score and grade
- Consumer Rating
- Restaruant Week Specials

Examples of data cleaning and transformation that we have performed are as follows:
- Removed restaurants that are not paricipating in restaurant week
- Dropped unnecessary data fields
- Filled in missing values
- Formatted fields
- etc. 

The tools that we used to clean up the data tables includes:
- Python
- Jupyter Notebook

**Load**:

After revaluating these information, we have created the following tables to provide further information in order to help consumers make their decisions. The tables can be found under "Final_Tables" folder:
- restaurant_2019_address
- restaurant_2019_cuisine
- restaurant_2019_inspec_grade
- restaurant_2019_neighborhood
- restaurant_2019_open_table_recommend
- restaurant_2019_yelp_review

The data tables are loaded to the Postgres database(postgres:postgres@localhost:5432/restaurant_week_db). The codes can be found under "Code" folder. 

By using the tables created and loaded to the database, we can answer the following questions:
- What are the restaurants participating in 2019 Restaurant Week?
- What are the top 10 restaurant types? How do the reviews say about the top 10 restaurant types?
- Which neighborhoods have have the most restaurants participating?
- Does neighborhood serve as the factor affecting the average review / ambience review / value review / food review / service review?
- Do Yelp reviews correlate with Open Table reviews?
