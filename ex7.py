def new_list(l1,l2):

    list3=[]
    index1=0
    while index1 < len(list1):
        index2=0
        while index2 < len(list2):
            if list1[index1] is list2[index2] :
                list3.append(list1[index1])
            index2+=1
        index1+=1
    return list3
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
print(new_list(list1,list2))