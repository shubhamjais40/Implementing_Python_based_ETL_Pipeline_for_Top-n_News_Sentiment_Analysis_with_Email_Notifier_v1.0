import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime
import sys
#sys.path.append(r'C:\Users\cvb\Documents\automation_python\etl_python')
from common import *

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def news_scraping(webpage:str):
    try:
        logging.info("Trying to connect data source..,")
        r=requests.get(webpage)
    except Exception as e:
        logging.error("Failed due to:",e)
    news=r.text
    return news



def beautifulsoup_extract_element(html_raw:str):
    soup=bs(html_raw,'html.parser')
    result=soup.find_all('ul',class_="story-list-ul")
    result=result[0]
    result=result.find_all('a')

    title=[]   #tile:news headline
    desc=[]    # Short summary of the news
    web_link=[] #Webink to access the news article page
    for i in range(len(result)):
        title.append(result[i].h3.text)
        desc.append(result[i].h4.text)
        web_link.append(result[i].get('href'))

    title=[item.strip() for item in title]  #cleaning spaces
    desc=[item.strip() for item in desc]
    #runtime timestamp for next update
    runtime=datetime.now().strftime("%x %H:%M") #formated with Date and Hr,min for every runtime
        
    newsframe_dic={"title":title,"short_summ":desc,"News_Link":web_link,"News_time":runtime}  #dict with all above lists
    df=pd.DataFrame(newsframe_dic)   #converting to dataframe with dict defined colmun names.
    return df

print("done")