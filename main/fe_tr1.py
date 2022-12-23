#fe_tr1 ==> reserved for front-end table reading
import pandas as pd
hard_d={}

#priority list
p_l=['DE001','TR002','LL003','PS004','KF005','SA006','CU007','SP008','AJ009','IS010','SB011','TP012','RP013']
def fr():
    global hard_d
    clone=[]
    n=1
    df=pd.read_csv('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv',encoding='ISO-8859–1')
    #make a copy of p_l list
    for i in p_l:
        clone.append(i)
    #list(df.columns
    #print(df.to_string()+'\n')
    #no of columns
    i=len(df.axes[1])
    #no of rows
    j=len(df.axes[0])
    list_3=[]
    for x in range(j):
        for y in range(len(clone)):
            
            if df.iat[x,0]==clone[y]:
                w=clone[y]
                if df.iat[x-1,0]==df.iat[x,0]:
                    n+=1
                    hard_d[w+str(n)]={}
                    hard_d[w+str(n)]['course']=[df.iat[x,1]]
                    hard_d[w+str(n)]['ca1']=[df.iat[x,2]]
                    hard_d[w+str(n)]['ca2']=[df.iat[x,3]]
                    hard_d[w+str(n)]['ca3']=[df.iat[x,4]]
                    hard_d[w+str(n)]['ca4']=[df.iat[x,5]]
                    hard_d[w+str(n)]['ca5']=[df.iat[x,6]] 
                else:
                    n=1
                    hard_d[w+str(n)]={}
                    hard_d[w+str(n)]['course']=[df.iat[x,1]]
                    hard_d[w+str(n)]['ca1']=[df.iat[x,2]]
                    hard_d[w+str(n)]['ca2']=[df.iat[x,3]]
                    hard_d[w+str(n)]['ca3']=[df.iat[x,4]]
                    hard_d[w+str(n)]['ca4']=[df.iat[x,5]]
                    hard_d[w+str(n)]['ca5']=[df.iat[x,6]]
    return()
fr()
print(hard_d)           








        #hard CAs


        # hard_d[df.iat[x,0]]=str(df.iat[x,7]).split(",")


    #print(x)
    
  
    
    #print(len(df.axes[0]))
#print(hard_d)
