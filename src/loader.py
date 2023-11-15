import os
from common import path_to_csv

def csv_loader(df):
    data=df
    final_frame=data.drop(columns=["pos","neu","neg","ids"])  #dropping unnecessary columns from final frame
    print("Appending Top-5 News to CSV file...")
    
    if os.path.exists(os.path.abspath(path_to_csv))==False:
        final_frame.to_csv(".\\loaded_data\\News.csv",mode='w', index=False, header=True)
    else:
        final_frame.to_csv(".\\loaded_data\\News.csv",mode='a', index=False, header=False)
    print("done")
    return 0

