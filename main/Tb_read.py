#Read generated tables
import pandas as pd
a=pd.read_csv('/Users/thejanhasaranga/Downloads/SampleCSVFile_2kb.csv', encoding='ISO-8859–1')
#print(a.to_string())
a=a.set_index('Eldon Base for stackable storage shelf, platinum')
print(a.to_string()+'\n')
print(a['3'][3])