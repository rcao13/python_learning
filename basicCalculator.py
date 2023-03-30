# Extra credit, come up questions in a group
# Dont know what question to come up with
print("Welcome to my first python program, here is an attempt to make a calculator")
correct = False
verison = input("Basic(1) or Advance(2) version? ")
operators = ['+','-','*','x','/','%']
match verison:
    case '1':
        while(not correct):
            in1 = input("Enter your first number in the calcuation: ")
            in2 = input("Enter your second number in the calcuation: ")
            op = input("Enter the operator for the calcuation: ").lower()
            prompt = input("Is your calcuation: "+ in1 + op + in2 + "? (y/n)\n")
            if prompt == "y" or prompt == "Y":
                correct = True
            else:
                print("Lets try again")
                correct = False
        match op:
            case '*':
                print("Result is: %0.2f" %(float(in1)*float(in2)))
            case 'x':
                print("Result is: %0.2f" %(float(in1)*float(in2)))
            case '+':
                print("Result is: %0.2f" %(float(in1)+float(in2)))
            case '-':
                print("Result is: %0.2f" %(float(in1)-float(in2)))
            case '/':
                print("Result is: %0.2f" %(float(in1)/float(in2)))
            case '%':
                print("Result is: %0.2f" %(float(in1)/float(in2)))
            case other:
                print("Sorry cannot interpret calculation")
    case '2':
        while(not correct):
            userInput = input("Enter your calculation, (ex. 20*20, 20x50): ")
            prompt = input("Is your calcuation: "+ userInput + "? (y/n)\n")
            if prompt == "y" or prompt == "Y":
                correct = True
            else:
                print("Lets try again")
                correct = False
        for i in operators:
            if i in userInput:
                vals = userInput.split(i)
                match i:
                    case '*':
                        print("Result is: %0.2f" %(float(vals[0])*float(vals[1])))
                    case 'x':
                        print("Result is: %0.2f" %(float(vals[0])*float(vals[1])))
                    case '+':
                        print("Result is: %0.2f" %(float(vals[0])+float(vals[1])))
                    case '-':
                        print("Result is: %0.2f" %(float(vals[0])-float(vals[1])))
                    case '/':
                        print("Result is: %0.2f" %(float(vals[0])/float(vals[1])))
                    case '%':
                        print("Result is: %0.2f" %(float(vals[0])/float(vals[1])))
                    case other:
                        print("Sorry cannot interpret calculation")
                break
                        