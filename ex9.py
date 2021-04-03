def harshad_number(num):
    sum=rem=0
    n=num
    while num>0:
        rem= num%10
        sum=sum+rem
        num=num//10
    if n%sum==0:
        print("It is a Harshad Number")
        return n
    else:
        print("it is not Harshad ")
        return n
number=int(input("Enter the number"))
print(harshad_number(number))
