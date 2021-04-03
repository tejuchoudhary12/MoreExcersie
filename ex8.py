def remove_duplicate(l1,l2):
    list3=list(set(list1+list2))
    return list3
         
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]

print(remove_duplicate(list1,list2))   