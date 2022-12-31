#this programme is to get an approch in order to create dictionaries from final output and show final results in tabularise manner also create a jason object2
def md(array1):
    md_l1=[]
    import fe_tr2
    import config
    import numpy as np
    array2=array1[:,0]
    for x in config.a:
        for y in array2:
            
            if y[:5]==x:
                md_l1.append(y)
    return(md_l1)
#a=md()
#print(a)

def order_a(df):
    #dc=[]
    import config
    import pandas as pd
    import numpy as np
    import csv
    #arr = np.array([])

    # Write the column names to a new CSV file
    with open('new_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Get the column names of the DataFrame
        headers = df.columns
        writer.writerow(headers)
    # Loop through the rows of the DataFrame
        for x in config.a:
            for index, row in df.iterrows():
    # Print the index and data for each row
                l1=row["ID"]
                if l1[:5]==x:
                #row_data = np.array(row)
                #arr = np.append(arr, row_data)
                    writer.writerow(row)
    
    #print(type(arr))