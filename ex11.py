# def convert(lst): 
#     return (lst[0].split()) 
  
# lst =  ["NavGurukul is an alternative to higher education reducing the barriers of current formal education system"] 
# print( convert(lst)) 

sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
a=[]
i=" "
for c in sentence:
    if c==" ":
        a.append(i)
        i=""
    else:
        i+=c
if i:
    a.append(i)
print(a)
        