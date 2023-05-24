option = int(input("1. Addition \n2.Subtraction \n3.Multiplication \n4.Division"))

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

match(option):

    case 1:
        print(num1+num2)
    
    case 2:
        print(num1-num2)

    case 3:
        print(num1*num2)
    
    case 4:
        print(num1/num2)

print("Done with this ass program")


