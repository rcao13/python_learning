# Extra credit, come up questions in a group
# Dont know what question to come up with
print("Welcome to my first python program, here is an attempt to make a calculator")
correct = False
while(not correct):
    in1 = input("Enter your first number in the calcuation: ")
    in2 = input("Enter your second number in the calcuation: ")
    op = input("Enter the operator for the calcuation: ")
    prompt = input("Is your calcuation: "+ in1 + op + in2 + "? (y/n)\n")
    if prompt == "y" or prompt == "Y":
        correct = True
    else:
        print("Lets try again")
        correct = False
match op:
    case '*':
        print("Result is: %0.2f" %(float(in1)*float(in2)))
    case '+':
        print("Result is: %0.2f" %(float(in1)+float(in2)))
    case '-':
        print("Result is: %0.2f" %(float(in1)-float(in2)))
    case '/':
        print("Result is: %0.2f" %(float(in1)/float(in2)))
    case other:
        print("Sorry cannot interpret calculation")