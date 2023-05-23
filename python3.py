marks = []
total = 0

def calcAverage (list):

    for item in list:
        total += list

    average = total/len(list)
    return average
    
mark = int(input("Enter marks of student: "))
marks.append(mark)

op = int(input("Do you want to put more marks? 1. Yes 2. NO"))

while (op == 1):
    mark = int(input("Enter marks of student: "))
    marks.append(mark)

    op = int(input("Do you want to put more marks? 1. Yes 2. NO"))
else:
    average = calcAverage(marks)
    print("The total marks of the students is ", total, " and average is ", average)

    


