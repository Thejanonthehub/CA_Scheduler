#This programme reads json file and store it as a dictionary
import json
import os
a=os.getcwd()
jc='%s/%s' % (a,'s2.json')
b={}
#Try_catch block  
try:
	with open(jc) as df:
		cp=json.load(df)
except IOError as e:
	print(e)
	print('IO Error')
	exit(1)
print(cp)