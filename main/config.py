#Convert config.txt vales into a dictionary 
import init
import numpy as np

dic_1={}
def con():
    global dic_1
    for x in range(len(init.vb_n)):
            dic_1[init.vb_n[x]]=init.value[x]

    return(dic_1)
con()
no_CA_t=dic_1['no_CA_t']
no_CA_l=dic_1['no_CA_l']
no_CA_p=dic_1['no_CA_t']
due=dic_1['due']
sem_month=dic_1['no_CA_t']
start_date=dic_1['no_CA_t']
start_month=dic_1['no_CA_t']
start_year=dic_1['no_CA_t']
max_ca=dic_1['no_CA_t']
p_l=dic_1['p_l']
a=p_l.split(sep=',')
fl1=dic_1['fl1']