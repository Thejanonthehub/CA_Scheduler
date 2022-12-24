class tree1:
    import pandas as pd
    import numpy as np
    df=pd.read_csv('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/test_data.csv',encoding='ISO-8859–1')
    array1=np.array(df)
    r,c=array1.shape
    def chk1(chk2):
        for i in range((tree1.r)):
            for j in range(1,6):
                x=tree1.array1[i][j]
                chk2(x)

        return()
    chk1()

    def chk2(t):
        global c
        c=-1
        for i in (tree1.array1):
            if t==i:
                c+=1
        print('we have '+ t+ 'as this many '+ str(c))
        return()
    chk2('2023-01-10')

