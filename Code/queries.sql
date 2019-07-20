-- Create tables for raw data to be loaded into

DROP TABLE restaurat_address;
DROP TABLE restaurant_cuisine;
DROP TABLE restaurant_inspection_results;
DROP TABLE restaurant_neighborhood;
DROP TABLE restaurant_open_table_review;
DROP TABLE restaurant_yelp_review;

CREATE TABLE restaurant_address (
id SERIAL PRIMARY KEY,
restaurant_name VARCHAR,
street_address VARCHAR,
google_map VARCHAR,
phone VARCHAR
);

CREATE TABLE restaurant_cuisine (
id SERIAL PRIMARY KEY,
restaurant_name VARCHAR,
cuisine VARCHAR
);

CREATE TABLE restaurant_inspection_results (
id SERIAL PRIMARY KEY,
restaurant_name VARCHAR,
inspection_score VARCHAR,
grade VARCHAR
);

CREATE TABLE restaurant_neighborhood (
id SERIAL PRIMARY KEY,
restaurant_name VARCHAR,
neighborhood VARCHAR
);

CREATE TABLE restaurant_open_table_review (
id SERIAL PRIMARY KEY,
restaurant_name VARCHAR,
percent_recommend INT
);

CREATE TABLE restaurant_yelp_review (
id SERIAL PRIMARY KEY,
restaurant_name VARCHAR,
average_review INT,
food_review INT,
service_review INT,
ambience_review INT,
value_review INT
);