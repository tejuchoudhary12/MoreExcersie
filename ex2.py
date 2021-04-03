def number():

    a=NumberOfExpenditure*NumberOfStudents
    if a<=50000:
        return "Budget: Rs.",a, "Hum budget ke andar hain "
    else:
        return "Budget: Rs.",a, "Hum budget ke bhar hai"

NumberOfStudents=int(input("Enter No. of. Students"))
NumberOfExpenditure=int(input("Enter the amount of expenditure"))

print(number())