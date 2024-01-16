## Table of Content

- Business Requirements

- Solution

- Tools/Technology Used

- Data Workflow Diagram

- ETL Description

- Challenges

- Future Recommendation

## Business/Client Problem:

A XYZ📲 is social media company which provides customer services like email marketing📧, news subscription,drop in prices notification etc. For engaging with subscribed customers they use channels like Facebook, Instagram and other third party vendors for SMS/mail push notifications. 


Well, They have some set of customers, subscribed for Top-5 news article from a leading News Medium via mail. The customer group is very time specific and mood oriented, they wish to get recommendation on type of News Psychological effects before reading, to only spend time in qualitative news articles rather than quantitative.

## Objective/Solution:

To setup & implement the data pipeline of code to automated workflow and achieve the business objective with News sentiment Analysis for improving the service quality and customer retention with Machine Learning Technique.

- Extracting the top news headlines from News Media using Web Scraping for each hour.
- Transforming the scrapped data to Table format with facts like: Headline, Short Description, Weblink and Mood Analysis (enhanced feature).
- Loading the table data to Excel Data Repositories for backup and along with processing the email with top news table to the subscribed customer.
- Automating the whole workflow to run each hour and implementing ETL concept to solve the problem with systematic approach.


## Tools & Technology:

- Python for Pipeline
- Mail Account of sender & receiver(One for Dev env)
- Docker (to run as isolated container)

## Data Workflow Diagram
![ETL_workflow](https://github.com/shubhamjais40/Implementing_Python_based_ETL_Pipeline_for_Top-n_News_Sentiment_Analysis_with_Email_Notifier_v1.0/blob/2f80cd4fb8bca2513ed2dc025559c1236feca09b/loaded_data/etl_diagram.png)

#### Python Lib Used:
`sys`
`os`
`requests`
`﻿beautifulsoup4`
`pandas`
`emails`
`smtplib`
`pretty-html-table`
`vaderSentiment`


## ETL Description

### Extract

- In Extract module,using news_scraping function, we can scrape the html content of the target webpage and this function will return string.

```python
def news_scraping(webpage:str):
    ....
    ....
    return <news : string>
```


- Now from news_scraping function html tags will be pushed to downstream beautifulsoup_extract_element module.
- Downstream module  would scrap required tags and class to find all news stories with headlines and description with adjoining runtime. Then further convert it to dataframe using pandas module as return.

```python
def beautifulsoup_extract_element(html_raw:str):
    ....
    ....
    return <table : dataframe> 
```
### Transform

- Now here comes important transform process using NLP technique,I used vaderSentiment module for analyzing sentiment of Each news short summary for extracted dataframe.
- This will take short summary of news and calculate positive, negative, neutral and compound average of sentiment factor, which is transformed to percentage format and merged with original dataframe.
- Since the end user could be any random recipient. Thus he may not able to interpret the sentiment factor % values, so we mapped the range of % factors directly to specific mood genre as per the category news article falls within.

```python
    def sentiment_key(x):
        if (x>0 and x<50):
            return "Neutral"
        elif x<0:
            return "Negative"
        else:
            return "Positive"
```


```python
def sentiment_analyzer(dataframe):
    return <transformed_dataframe> 
```


### Loader

- After the transformed data in a returned dataframe, its time to load the data in a specific file format/cloud storage.
- Here I loaded valuable transformed table in CSV file format into loaded_data directory within project.


```python
def csv_loader(df):
    return None

```

### Enhancement with Email functionality

- Final transformed dataframe from upstream would be using pretty_html_table lib to format as a html table and delivered to the end user for every runtime of Data Pipeline.

```python
def do_email(dataframe):
    return None
```
![Email_workflow](https://github.com/shubhamjais40/Implementing_Python_based_ETL_Pipeline_for_Top-n_News_Sentiment_Analysis_with_Email_Notifier_v1.0/blob/2f80cd4fb8bca2513ed2dc025559c1236feca09b/loaded_data/output.JPG)
### Pipeline runner

Pipeline workflow is implemented with Python module etl_run.py . Logging is also used to track ETL pipeline failure in any case so to debug easily.
In Linux Environment, cron job can be setup with job_scheduler.sh to run, every hour as articles usually gets latest feeds.

## Challenges
- HTML tags scraping and extracting required tags using BeautifulSoup lib.
- Sentiment analysis of news article and transforming using sentiment function to categorize into positive,neutral & negative articles.
- Using pandas to format overall json based data structure to dataframe.
- Preparing dataframe to HTML table format using MIME lib and sending email notification.
- Scheduling etl_run file using cron job which has to be run at every hour. [* */1 * * *]
- Loading data locally as CSV file.

## Future Recommendation

- For more accurate sentiment analysis, we can go for Naive Bayes, TextBlob, Deep Learning LSTM NLP models. 

- For scalable workloads and complex scheduling, Data Pipeline tools could be used such as Airflow, AWS Pipeline,etc.
