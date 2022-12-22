#Read generated tables
list_2=[]
def r_t():
    import pandas as pd
    global list_2
    a=pd.read_csv('/Users/thejanhasaranga/CA_Scheduler/main/csv_files/DAC_lec.csv', encoding='ISO-8859–1')
    #print(a.to_string())
    #a.set_index('Instructor Code')
    list(a.columns)
    
    print(a.to_string()+'\n')
    

    #creating dictionary including lecturer code and the priority level
    tb_l=len(a)
    for x in range(1,tb_l):
        list_2.append(a.iat[x,0])
        
    return()
r_t()
print(list_2)
