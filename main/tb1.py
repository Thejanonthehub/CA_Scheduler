import pandas as pd
df1=pd.read_csv('DAC_lec.csv')
p_l=df1[(df1['Priority Level']==3)]
print(len(p_l))
