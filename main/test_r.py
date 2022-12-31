def stol(dp1,st1): #convert string reprentation of a list to actual list
    import re
    import ast
    a=dp1[st1]
    a=a.replace(', nan', '')
    a = ast.literal_eval(a)
    return(a)

#insert 'Nan' to spaces inside dictionary 'dx'
def nan(dx):
    import date_booking
    import fe_tr2
    keys = dx.keys()
    for x in keys:
        a=dx[x]
        b=len(a)
        f=fe_tr2.n_co
        rv=f - b
        for y in range(rv-1):
            dx[x].append('NaN')
    #print(dx)
    return(dx)


