#this programme is to get an approch in order to create dictionaries from final output and show final results in tabularise manner also create a jason object2
def md(array1):
    md_l1=[]
    import fe_tr2
    import config
    import numpy as np
    for y in array1:
        md_l1.append(y)
    return(md_l1)
#a=md()

#reform original csv out from the mysql according to the priority level based manner
def order_a(df):
    #dc=[]
    import config
    import pandas as pd
    import numpy as np
    import csv
    import os

    # Delete existing csv file called 'new_data.csv' if there any
    main='/Users/thejanhasaranga/CA_Scheduler/main'
    """if 'new_data.csv' in main:
        os.remove('new_data.csv')"""

    # Write the column names to a new CSV file
    with open('new_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Get the column names of the DataFrame
        headers = df.columns
        writer.writerow(headers)
    # Loop through the rows of the DataFrame
        for x in config.a:
            for index, row in df.iterrows():
    # index and data for each row
                l1=row["ID"]
                if l1[:5]==x:
                    writer.writerow(row)        
