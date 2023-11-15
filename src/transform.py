

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd



def sentiment_analyzer(dataframe):
    f=dataframe
    sia = SentimentIntensityAnalyzer()
    ids=[]
    neg=[]
    pos=[]
    neu=[]
    compound=[]
    for i,row in (f.iterrows()):
        #print(i,row['Short_sum'])
        score_dict=sia.polarity_scores(row['short_summ'])
        ids.append(i)
        neg.append(score_dict['neg'])
        pos.append(score_dict['pos'])
        neu.append(score_dict['neu'])
        compound.append(score_dict['compound'])
        
    #DataFrame is created using news id as primary key to map with our first news extracted dataframe df.
    sentiment_frame=pd.DataFrame(list(zip(ids,pos,neu,neg,compound)),columns =['ids', 'pos','neu','neg','compound'])

    final_frame=pd.merge(f, sentiment_frame,  left_index=True, right_index=True)  #merged on index
    final_frame['compound']=final_frame['compound']*100.0
    
    #sentiment_key--> a nested funcion to entitle news with mood genre based on compound score.
    def sentiment_key(x):
        if (x>0 and x<50):
            return "Neutral"
        elif x<0:
            return "Negative"
        else:
            return "Positive"
    final_frame['Mood']=final_frame['compound'].apply(sentiment_key)
    return final_frame   #table with news atttributes+mood genre


#print(sentiment_analyzer())