# Finance_News_Sentiment

![image](https://d1sjtleuqoc1be.cloudfront.net/wp-content/uploads/2019/04/25112909/shutterstock_1073953772-860x574.jpg)

## Table of Contents ##
* [Project Proposal](#project-proposal)
* [Data Source](#data-sources)
* [Technologies](#technologies)
* [Machine Learning Steps](#machine-learning-steps)
* [Using Machine](#using-machine)
* [Full Stack Flow](#Full-Stack-Flow)
* [Example Queries](#example-queries)
* [Team Roles](#team-roles)

## Project Proposal 
# A brief description of your final database
Using machine learning, create an algorithm that would take financial headlines as an input and analyze current sentiment in the financial industry. 

# Why our final sentiment analysis will be useful to users?
1) Using financial headline inputs in csv format, users can get an analysis with classification of each inputted financial headline. 
2) Using additional Stock News API data (date and tickers), stock list csv file, and our Tableau dashboard template, users can perform additional anaylsis on the following:
  a) Sentiment analysis a given time period
  b) Sentiment analysis by companies, sectors and industry
  c) Emotional Analysis by keywords
  d) Word Blast
  
## Data sources
1) [Stock News National Park Services API](https://stocknewsapi.com/documentation)  <br>
2) [Stock List with Ticker, Country, Exchange, Financai Sector and Industry details](https://www.nasdaq.com/market-activity/stocks/screener)<br>

 
## Technologies
* Python Pandas
* Tableau
* PySpark / Google Colab
* ScikitLearning
* JavaScript
* HTML/CSS

### Machine Learning Steps 
1) Get Test Data (https://stocknewsapi.com/documentation) to retrieve financial headlines and sentiment classification and save as csv <br>
  [Get API key](https://stocknewsapi.com/register)<br>
  
2) Read Test Data in as DataFrame <br>

3) Tokenization - Break financial headlines into a list of words <br>

4) Countvectorizer - Generate the term frequency vectors

5) Inverse Document Frequency - Down-weighs features which appear frequently in a corpus.

6) Split Data - Train 80%, Test 20%

7) Hypertuning and Model - Logistics Regression and Naive Bayes to compare accuracy, F1 score. Hypertune with Param Grid Search and Cross Validator.

  
### Using Machine <br>
1) Get financial headlines from Stock New API or use alternative dataset <br>
2) Read dataset in as DataFrame <br>
3) Run the notebook for with the NLP model to retrieve sentiment classification for each headline <br>


### Data Analysis <br>
1) Get date and ticker information from Stock News API or use alternative dataset <br>
2) Use Stock List from NASDAQ with key ticker information <br>
3) Run the notebook for to clean and merge the financial sentiment classification, date, and detailed ticker information to perform analysis <br>
4) Save merged DataFrame as csv <br>
5) Open csv in Tableau, using template provided, view data visualization. <br>

The below to be updated
### Load<br>
1) Create database called park_db
2) [Create tables using the schema file](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/ERD/erd_schema.sql)<br>
3) Load csv files into Postgres database<br>

## Steps to recreate database
### Option 1 - Import to Postgres using provided notebook<br>
1) Create config.py file with postgres username, password <br>
2) [Create tables using the schema file](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/ERD/erd_schema.sql) The database should be named "park_db"<br>
3) Run [import_csvs_to_db.ipynb](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/import_csvs_to_db.ipynb) file<br>

### Option 2 - Manual data import to Postgres<br>
1) Create config.py file with postgres username, password <br>
2) Access the park tables from the [Resources folder](https://github.com/adriana-icasiano/yogi_booboo_playground/tree/main/Resources):<br>
3) [Create tables using the schema file](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/ERD/erd_schema.sql) The database should be named "park_db"<br>
4) Import the data into the table in this order:<br>
[park data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/nps_park_data_final.csv) <br> 
[activity data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/activities_data.csv)<br>
[park activity data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/park_activities_data.csv)<br>
[fee data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/fee_id_data.csv)<br> 
[park fee data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/park_fee_data.csv)<br>
[scientific name data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/sci_name_latest.csv)<br>
[park species data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/park_species_latest.csv)<br>
[fire data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/wildfires.csv)<br>
[park images data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/images_data.csv)<br>
[park live webcam data](https://github.com/adriana-icasiano/yogi_booboo_playground/blob/main/Resources/webcam_data.csv)<br>

## Full Stack Flow<br>
In addition to the Home route within Flask we have created 5 other routes, the below describes the routes and the associated javascript files:<br>
1.) "/park" -->	park.js<br>
2.) "/wildfires" -->	fires.js, fire_size.js<br>
3.) "/activity" -->	activity.js<br>
4.) "/activity_count" -->	activity.js<br>
5.) "/fireclass" -->	fireclass.js<br>
6.) "/species" -->	species.js, counts.js<br>

Flask then renders to the Index.html file.

## Example Queries                                                        
## Tables:
```sql
SELECT * from park;
SELECT * from activity;
SELECT * from park_activity;
SELECT * from fees;
SELECT * from park_fee;
SELECT * from images;
SELECT * from webcam_url;
SELECT * from fire;
SELECT * from sci_name;
SELECT * from park_species;
```                                                        
                                                        
### To retrieve a list of National Parks that are free and paid:
```sql
SELECT p.* , p.park_name, f.fee
FROM fees as f
JOIN park_fee as pf                        
ON f.fee_id = pf.fee_id
RIGHT JOIN park as p
ON p.park_id = pf.park_id
```                                                                                                                       

### To retrieve all wildfires at National Parks in the last 24 fires:
```sql
SELECT f.* ,p.park_name
FROM fire as f
JOIN park as p
ON f.park_id = p.park_id
```                                                           

### To retrieve scientific name, order, family and category information on species at National Parks:
```sql                                                        
SELECT p.park_name, sn.*, ps.*
FROM park_species as ps
JOIN sci_name as sn
ON ps.sci_name_id = sn.sci_name_id
JOIN park as p
on ps.park_id = p.park_id
```  
                                                        
#### Team Roles

| Team Member           | Github username  |        
| -----------           | -----------
| Adriana Icasiano      | adriana-icasiano |
| Paul Feliciano        | pfeliciano1      |
| Alberto Gonzalez      | dalismo          |
| Abayomi Olujobi       | bay0624          |
| Lovensky Lubin        | Lubinl           |

