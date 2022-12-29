import fe_tr2

'''with open("confirmed_dates.csv",mode="w") as csvfile:
        ca=fe_tr2.n_co
        fieldnames=["ID","Confirmed_Dates"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()'''
import csv

# Open the CSV file in read mode
with open('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Get the headers from the first row
    headers = next(reader)
    
    # Print the headers
    print(headers)
