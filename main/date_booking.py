def da_chk(d_l,lv,id):
    import config
    import fe_tr2
    a_l8=[]
    d_l3={}
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
    
    if int(d_l[lv])<=int(config.due):
        print(lv, ' Date booked by ',id)
        
    else:
        if d_l4[lv]<int(config.due):
            for it2 in a_l8:
                if lv==it2:
                    d_l4[lv]+=1
                    print('date ',lv,' is booked by 2nd loop')
        else:
            print('date is already booked')
    return()
    
#da_chk(fe_tr2.d_l,'2021-01-10')