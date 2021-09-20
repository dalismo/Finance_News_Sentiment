# Finance_News_Sentiment

![image](https://user-images.githubusercontent.com/78628287/133952518-aa7a1665-d9ca-490e-bce4-2cb44380cb6e.png))

## Table of Contents ##
* [Project Proposal](#project-proposal)
* [Data Source](#data-sources)
* [Technologies](#technologies)
* [Machine Learning Steps](#machine-learning-steps)
* [Using Machine](#using-machine)
* [Team](#team)



## Project Proposal 
# A brief description of our project
Using machine learning, create an algorithm that would take financial headlines as an input and analyze current sentiment in the financial industry. The analysis would be particularly interesting in the context of the Covid pandemic.

# Why our final sentiment analysis will be useful to users?
1) Using financial headline inputs in csv format, users can get an analysis with classification of each inputted financial headline. 
2) Using additional Stock News API data (date and tickers), stock list csv file, and our Tableau dashboard template, users can perform additional anaylsis on the following: <br>
  a) Sentiment analysis a given time period <br>
  b) Sentiment analysis by companies, sectors and industry <br>
  c) Emotional Analysis by keywords <br>
  d) Word Blast <br>
  
## Data sources
1) [Stock News National Park Services API](https://stocknewsapi.com/documentation)  <br>
2) [NASDAQ List - Ticker, Country, Exchange, Financai Sector and Industry details](https://www.nasdaq.com/market-activity/stocks/screener)<br>

 
## Technologies
* Python Pandas
* Tableau
* PySpark / Google Colab
* ScikitLearning
* JavaScript
* HTML/CSS
* [w3schools.com](https://www.w3schools.com/spaces/)
* [cloudtables.com](https://berrb9rr1p.cloudtables.com/login)

### Machine Learning Steps 
1) [Get Test Data](https://stocknewsapi.com/documentation) to retrieve financial headlines and sentiment classification and save as csv <br>
  [Get API key](https://stocknewsapi.com/register)<br>
  
2) Read Test Data in as DataFrame <br>

3) Tokenization - Break financial headlines into a list of words <br>

4) Countvectorizer - Generate the term frequency vectors

5) Inverse Document Frequency - Down-weighs features which appear frequently in a corpus.

6) Split Data - Train 80%, Test 20%

7) Hypertuning and Model - Run [Machine Notebook](). The notebook runs the test data through both the Logistics Regression and Naive Bayes, applies hypertuning with Param Grid Search and Cross Validator and allows users to evaluate the models using area under ROC, accuracy, F1 score. 

  
### Using Machine Learning Model
1) Get financial headlines from Stock New API or use alternative dataset <br>
2) Read dataset in as DataFrame <br>
3) Run the model from above to retrieve sentiment classification for each headline <br>


### Data Analysis <br>
1) [Get date and ticker information from Stock News API](https://stocknewsapi.com/documentation) or use alternative dataset<br>
2) Use [Stock List from NASDAQ with key ticker information](https://www.nasdaq.com/market-activity/stocks/screener) <br>
3) Run the [functions notebook](https://github.com/dalismo/Finance_News_Sentiment/blob/main/functions.py) to clean and merge the financial sentiment classification, date, and detailed ticker information to perform analysis <br>
4) Save merged DataFrame as csv <br>
5) Open csv in Tableau, using template provided, view data visualization. <br>

                                                        
#### Team 

| Team Member           | Github username  |        
| -----------           | -----------
| Adriana Icasiano      | adriana-icasiano |
| Paul Feliciano        | pfeliciano1      |
| Alberto Gonzalez      | dalismo          |
| Abayomi Olujobi       | bay0624          |
| Lovensky Lubin        | Lubinl           |

