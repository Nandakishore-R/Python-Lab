while(True):
    a = int(input("Enter first number : "))
    b = int(input("Enter 2ns number : "))
    op = input("Enter which operation \n +,-,*,/  : ")
    if(op == '+'):
     print(a,' + ',b," is : ",a+b)
    elif(op == '-'):
        print(a,' - ',b," is : ",a-b)
    elif(op == '*'):
        print(a,' * ',b," is : ",a*b)
    elif(op == '/'):
        if(int(b) != 0):
            print(a,' / ',b," is : ",a/b)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter either +, -, * or /")
    