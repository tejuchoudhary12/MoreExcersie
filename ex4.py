FirstNumber=int(input("Enter the number"))
SecondNumber=int(input("Enter the number"))
ThirdNumber=int(input("Enter the number"))

def find_Biggest():      
     if(FirstNumber>=SecondNumber) and (FirstNumber>=ThirdNumber):
         largest=FirstNumber
     elif(SecondNumber>=FirstNumber) and (SecondNumber>=ThirdNumber):
         largest=ThirdNumber
     else:
         largest=ThirdNumber
     print("Largest number is",largest)

find_Biggest()
