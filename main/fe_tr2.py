#front-end table reading programme two...
import pandas as pd
import numpy as np
from math import nan

#import fe_tr1
p_l2=['DE001','TR002','TR002','CU007']
#Convert 'test_data.csv' file into a numpy array
df=pd.read_csv('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv')
#,encoding='ISO-8859–1'
#print(df)
array1=np.array(df)


#pd.DataFrame(array1).drop_duplicates().values
#print(array1)
#get no. of rows and columns of numpy array
r,c=array1.shape
print(r,c)
n=0
c=0
de_l=[]
for j in range(r):
    a=array1[j][0]
    if a[:5]==p_l2[1]:
        n+=1
        de_l.append(a)

    for i in range(c):
        print('pass')
#print(de_l)


def se():
    pt=0
    lc=''
    for x in de_l:
        if int(x[11])==1:
            pt==int(x[9:12])
            lc=x
            continue
        else:
            if int(x[9:12])<pt:
                pt=int(x[9:12])
                lc=x
        print(lc)
    return(pt)

#se()
#print(array1)
#lecture code recognition
def chk1():
    for i in range(r):
        for j in range(1,6):
            l=array1[i][j]
            chk2(l)
    return()

def chk2(t):
    c=1
    #for i in array1:
    copy_array1=np.copy(array1)
    copy_array1=array1[:,0:6] 
    #r2,c2=copy_array1.shape
    for x in copy_array1:
        if x==t:
            c+=1
                    #copy_array1=np.delete(copy_array1,np.where(copy_array1==copy_array1[i][j]))

    print('we have '+ str(t)+ 'as this many '+ str(c))
    #print(copy_array1)
    return()
#chk2('2023-01-10')
#chk1()
copy_array1=np.copy(array1) #make a copy from array1
copy_array1=array1[:,1:6] #limit it to a particular data range
a_l=copy_array1.tolist() # convert to a list
a_l3=[]
a_l2=[]
def uqe(): #this list for creating unnique date list from the test_data file
    global a_l2
    global a_l3

    #get it to a plain list (not cluters inside)
    for q in a_l:
        for e in q:
            a_l2.append(e)
    print(len(a_l2))

    # insert equal items to the list a_l3
    for i in a_l2:
        if str(i)=="nan":
            break
        if i not in a_l3:
            a_l3.append(i)
        else:
            print(i,'\n')
    return(a_l3)
uqe()

def eq():# this fuction is to calculate how many uequal dates are there
    c=0
    d_l={}
    for i in a_l3:
        for j in a_l2:
            if i==j:
                c+=1
        d_l[i]=c
        c=0
    print(d_l,"\n")
    return()
eq()
print(len(a_l2))
print(len(a_l3))

#result,indices=np.unique(array1,return_index=True)

#print(result)  