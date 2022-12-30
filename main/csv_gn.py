


'''with open("confirmed_dates.csv",mode="w") as csvfile:
        ca=fe_tr2.n_co
        fieldnames=["ID","Confirmed_Dates"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()'''

def crt_csv(id,lv):
    import csv
    import pandas as pd
    import numpy as np
    import date_booking
    with open('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv', 'r') as f:
        # Create a CSV reader object
        reader = csv.reader(f)

        # Get the first row (the headers)
        headers = next(reader)

        # Convert the headers to a list
        headers = list(headers)
        headers_c=headers[:len(headers)-2] # this is for seperating Id and all CAs from flexible & hard columns
        import csv

        # Open the CSV file in write mode
        with open('confirmed_dates.csv', 'w', newline='') as f:
        # Create a CSV writer object
            writer = csv.writer(f)
            
            # Write the headers
            writer.writerow(headers_c)

    print(headers_c)
    return()
crt_csv()