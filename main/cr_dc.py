#this programme is to get an approch in order to create dictionaries from final output and show final results in tabularise manner also create a jason object
md_l1=[]
def md():
    global md_l1
    import fe_tr2
    import config
    for x in config.p_l:
        for y in fe_tr2.array2:
            if x==y[0:5]:
                md_l1.append(y)
            
    print(md_l1)   
md()