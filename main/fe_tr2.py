#front-end table reading programme two...
import pandas as pd
import numpy as np
from math import nan
import cr_dc

df0=pd.read_csv('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv')
#,encoding='ISO-8859–1'

cr_dc.order_a(df0)
df=pd.read_csv('new_data.csv')
array1=np.array(df)
array2=array1[:,0] #sub array- Lecturers Id#array2=cr_dc.md(array1) #pass array1 to function 'md' in 'cr_dc' file to list lecturer id according
 
#get no. of rows and columns of numpy array
r,co=array1.shape
n_co=co-2 #without hard and flexible columns

#create dictionary to store dates based on ids
copy_array3=array1[:,0:6]
a_l4=copy_array3.tolist()
d1={} # this dictionary consists of ID and dates 
def cd():
    global d1
    for cl in a_l4:
        d1[cl[0]]=str(cl[1:])
    #print(d1)  
    return()
cd()
copy_array1=np.copy(array1) #make a copy from array1
copy_array1=array1[:,1:6] #limit it to a particular data range
copy2_array1=array1[:,0:6]
a_l5=copy2_array1.tolist()
a_l=copy_array1.tolist() # convert to a list
a_l3=[]
a_l2=[]
def uqe(): #this list for creating unnique date list from the test_data file
    global a_l2
    global a_l3
    #get it to a plain list (not clusters inside)
    for q in a_l:
        for e in q:
            if str(e)=="nan":
                break
            a_l2.append(e)

    # insert equal items to the list a_l3
    for i in a_l2:
        if str(i)=="nan":
            break
        if i not in a_l3:
            a_l3.append(i)
        '''else:
            print(i,'\n')'''

    return(a_l3)
uqe()

d_l={}
def eq():# this fuction is to calculate how many uequal dates are there
    c=0
    global d_l
    for i in a_l3:
        for j in a_l2:
            if i==j:
                c+=1
        d_l[i]=c
        c=0
    #print(d_l,"\n")
    return()
eq()

