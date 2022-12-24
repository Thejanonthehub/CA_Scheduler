#initializing...
#read a file called config.txt where it stored default values defined by the administration 
a=[]
b=[]
vb_n=[]
value=[]
def i():
    global vb_n
    global value
    import pandas as pd
    import numpy as np
    df=pd.read_table('config.txt',sep=',')
    #df.set_index('variable_name')
    #print(df,'\n')
    #table length
    tb_l=len(df)
    for x in range(tb_l):
        vb_n.append(df.iat[x,0])
    for y in range(tb_l):
        value.append(df.iat[y,1])
    #creating 2d numpy array inserting arrys 'vb_n' and 'value'
    global a
    global b
    a=np.array([vb_n])
    b=np.array([value], dtype=str)

    #print(a)
    
    return(a,b)
#print(i())
i()
#print(b.dtype)
#print(vb_n)