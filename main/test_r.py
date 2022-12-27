def stol(dp1,st1): #convert string reprentation of a list to actual list
    import re
    import ast
    a=dp1[st1]
    a=a.replace(', nan', '')
    a = ast.literal_eval(a)
    return(a)
