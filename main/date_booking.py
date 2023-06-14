#this programme for priority checking and the booking data based on that
def dt_chk():
    import fe_tr2
    import test_r
    import config
    import test_r
    import copy
    import csv_gn
    import pandas as pd
    import cr_json
    a_l6=[] 
    a_l8=[]
    d_l3={}
    d1_copy = copy.copy(fe_tr2.d1)
    a_l7 = [item for item in fe_tr2.a_l2 if 
    fe_tr2.a_l2.count(item) > int(config.due)]
    for it1 in a_l7:
        if it1 not in a_l8:
            a_l8.append(it1)
    cv=0
    for rt in a_l8:
        for rq in a_l7:
            if a_l7==a_l8:
                cv+=1
            d_l3[rt]=cv
            cv=0
    d_l4 = {key: 0 for key in d_l3}
     
    for id in fe_tr2.array2:# array2-lecturer id from csv
        l1=[]
        for d in fe_tr2.a_l3: #dates from unique date list a_l3
                    a_l6=test_r.stol(fe_tr2.d1,id) #passing object to function 'stol'
                    for lv in a_l6: # lecturers input dates from a_l2
                        if lv=="nan":# removing 'nan'
                            break
                        if lv==d: #chek whether di equals to d
                            cnt=int(fe_tr2.d_l[lv])
                            if int(fe_tr2.d_l[lv])<=int(config.due):
                                l1.append([str(lv)+' - ✓ booked'])
                            else:
                                if d_l4[lv]<int(config.due):
                                    for it2 in a_l8:
                                        if lv==it2:
                                            d_l4[lv]+=1
                                    l1.append([str(lv)+' - ✓ booked'])
                                else:
                                    l1.append([str(lv)+" - Sorry, The date is already booked"])
    
        d1_copy[id]=l1
    #print(df3)'''
    d1_copy=test_r.nan(d1_copy)
    csv_gn.crt_csv(d1_copy) #passing d1_copy to...
    df3= pd.DataFrame(d1_copy) # dictionary to data frame
    df3.to_csv('confirmed_dates.csv', index=True) #convert data frame to a csv 
    df4 = pd.read_csv('confirmed_dates.csv', index_col=1) #read created csv file
    print(df4) #output
    cr_json.js(d1_copy) # creating json object                    
    return() 
dt_chk()  
#for testing purposes