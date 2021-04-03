def list1():

    i=1
    list=[]
    while i<=23:
        if i%3==0:
            print( i, "nav")
        if i%7==0:
            print( i, "Gurukul")
        if i%21==0:
            b=i, "Navgurukul"
            list.append(b)
        i+=1
    print(list)

list1()


# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
# i=0
# while i<len(list1):
#     if list1[i]%3==0:
#         print(list1[i],"nav")
#     if list1[i]%7==0:
#         print(list1[i],"gurukul")
#     if list1[i]%21==0:
#         print(list1[i],"navgurukul")
#     list2.append(list1[i])
#     i+=1
# print(list2)

# def list1():

#     i=1
#     # list=[]
#     while i<=10:
#         if i%3==0:
#             print( i, "Nav")
#         if i%7==0:
#             print( i, "Gurukul")
#         if i%21==0:
#             print( i, "NavGurukul")
        
#     print(i)
#     i+=1
    
# list1()

