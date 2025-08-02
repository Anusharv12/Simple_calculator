def calculator():
    print("Simple Calculator")
    print("Choose Operation: + - * /")
    try:
        num1=float(input("\nEnter first number: "))
        operator=input("Enter operator(+ - * /): ")
        num2=float(input("Enter second number: "))
        if operator=="+":
            result=num1+num2
        elif operator=="-":
            result=num1-num2
        elif operator=="*":
            result=num1*num2
        elif operator=="/":
            if num2!=0:
                result=num1/num2
            else:
                print("Error: Can't divided by zero")
                return
        else:
            print("Invalid operator")
            return
        print("Result: ",result)
    except ValueError:
        print("Invalid input,please enter numbers only")
calculator()
        