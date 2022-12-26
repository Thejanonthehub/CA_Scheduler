#front-end table reading programme two...
import pandas as pd
import numpy as np
from math import nan
import csv
import config
#
p_l=['DE001','TR002','LL003','PS004','KF005','SA006','CU007','SP008','AJ009','IS010','SB011','TP012','RP013']

#import fe_tr1
#Convert 'test_data.csv' file into a numpy array
df=pd.read_csv('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv')
#,encoding='ISO-8859–1'
#print(df)
array1=np.array(df)
array2=array1[:,0] #sub array- Lecturers Id
print(array2)

#pd.DataFrame(array1).drop_duplicates().values
#print(array1)
#get no. of rows and columns of numpy array
r,co=array1.shape
#print(r,c)

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

n=0
c=0
de_l=[]
for j in range(r):
    a=array1[j][0]
    if a[:5]==array2[1]:
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
        #print(lc)
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
copy2_array1=array1[:,0:6]
a_l5=copy2_array1.tolist()#******************************************
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
'''print(len(a_l2))
print(len(a_l3))'''
#print(array1)
#result,indices=np.unique(array1,return_index=True)

def prior2(vl1):
    import config
    for x in a_l3:
        if int(d_l[x])>int(config.due):
            print('should check for priority')
        else:
            print("date booked for ",vl1)
    return()


#print(result) 
def cmp():
    import test_r
    import config
    import csv
    rc=1
    d_l2={}
    a_l6=[]
    ro=array2.shape
    #get column names
    #frm=df.columns.values.tolist()
    
    #open a csv file 
    with open("confirmed_dates.csv",mode="w") as csvfile:
        fieldnames=["ID","Confirmed_Dates"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for co in config.a:# values from the priority list in config file
            for id in array2:# array2-lecturer id from csv
                if id[:5]==co: #match the lecturer code with priority list
                    if int(id[9:12])>=rc:#check the assessment number ...001
                        rc=int(id[9:12])
                        print("call ",id)
                        
                        for d in a_l3: #dates from unique date list a_l3
                            a=d1[id]
                            a_l6=test_r.stol(d1,id) #passing object to function 'stol'
                            #print(a_l6)
                            for lv in a_l6: # lecturers input dates from a_l2
                                if lv=="nan":# removing 'nan'
                                    break
                                if lv==d: #chek whether di equals to d
                                    if int(d_l[lv])<=int(config.due):
                                        print('Date booked ',lv)
                                        


                                    
                #writer.writerow({"ID":"b","Confirmed_Dates":"2023-01-02"})
    return() 
cmp()



#print(frm)
print(a_l2)
#print(a_l3)
#print(array2)
#print(d1) ****
#print(array1)
#print(d_l) ****

'''for um in range(len(a_l5)):
    if a_l5[um][0]=='DE001ETEC001':
        print(a_l5[um][1:])'''


