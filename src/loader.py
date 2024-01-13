import os
#from common import path_to_csv

def csv_loader(df,loader_path):
    final_frame=df.drop(columns=["pos","neu","neg","ids"])  #dropping unnecessary columns from final frame
    print("Appending Top-5 News to CSV file...")
    
    if os.path.exists(os.path.abspath(loader_path))==False:
        final_frame.to_csv(os.path.abspath(loader_path),mode='w', index=False, header=True)
    else:
        final_frame.to_csv(os.path.abspath(loader_path),mode='a', index=False, header=False)
    print("done")
    return None

