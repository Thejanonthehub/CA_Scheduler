#this programme for priority checking and the booking data based on that
def dt_chk():
    import fe_tr2
    import test_r
    import config
    import test_r
    import copy
    import csv_gn
    import pandas as pd
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
        print("call ",id)
        for d in fe_tr2.a_l3: #dates from unique date list a_l3
                    a_l6=test_r.stol(fe_tr2.d1,id) #passing object to function 'stol'
                    #print(a_l6)
                    for lv in a_l6: # lecturers input dates from a_l2
                        if lv=="nan":# removing 'nan'
                            break
                        if lv==d: #chek whether di equals to d
                            cnt=int(fe_tr2.d_l[lv])
                            if int(fe_tr2.d_l[lv])<=int(config.due):
                                print(lv, ' Date booked')
                                l1.append([str(lv)+' - booked'])
                                #writer.writerow('Id':'j')
                            else:
                                if d_l4[lv]<int(config.due):
                                    for it2 in a_l8:
                                        if lv==it2:
                                            d_l4[lv]+=1
                                    print('date ',lv,' is booked by 2nd loop')
                                    l1.append([str(lv)+' - booked'])
                                else:
                                    print(lv,'date is already booked')
                                    l1.append([str(lv)+" - already booked"])
    
        d1_copy[id]=l1
    #print(df3)'''
    d1_copy=test_r.nan(d1_copy)
    csv_gn.crt_csv(d1_copy)
    df3= pd.DataFrame(d1_copy)
    df3.to_csv('confirmed_dates.csv', index=True)  
    df4 = pd.read_csv('confirmed_dates.csv', index_col=2) 
    print(df4)                      
    #print(d_l4)                         
      #writer.writerow({"ID":"b","Confirmed_Dates":"2023-01-02"})
    return() 
#dt_chk() for testing purposes