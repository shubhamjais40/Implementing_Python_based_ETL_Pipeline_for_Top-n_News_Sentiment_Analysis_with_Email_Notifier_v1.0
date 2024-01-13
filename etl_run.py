import sys
import logging
sys.path.append(r'./src/')
from extract import news_scraping,beautifulsoup_extract_element
from transform import sentiment_analyzer
from common import weblink,path_to_csv,sender,receiver
from loader import csv_loader
from email_feature import do_email


logging.basicConfig(format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.debug('This will get logged')


def main():
    raw=news_scraping(weblink)
    logging.info("News extracted..")
    df1=beautifulsoup_extract_element(raw)
    logging.info("News extracted transformed..")
    processed_df=sentiment_analyzer(df1)
    logging.info("Sentiment analyzed transformed..")
    csv_loader(processed_df,path_to_csv)
    logging.info("CSV Loaded successfully..")
    logging.info(processed_df)
    #do_email(processed_df,sender,receiver)
    logging.info("email_sent successfully...")

if __name__=="__main__":
    main()

