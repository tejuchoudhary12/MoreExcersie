san=input("enter your santance")
a=""
word=san.split()

for i in word:
    if len(a)>0:
        a=a+" "+ i.capitalize()
    else:
        a=i.capitalize()
print(a)