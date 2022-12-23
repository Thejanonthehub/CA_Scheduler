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
print(dic_1)