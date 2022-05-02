
#faulty Calculator
firstNum = int(input("Enter First Number "))
operation = input("Enter Which Operation do you want to perform ")
secondNum = int(input("Enter Second Number "))

if operation == "+":
    if firstNum == 56 and operation == "+" and secondNum == 9:
        result = 77
    else:
        result = firstNum + secondNum
elif operation == "-":
    result = firstNum - secondNum
elif operation == "/":
    if firstNum == 56 and operation == "/" and secondNum == 6:
        result = 4
    else:
        result = firstNum / secondNum
elif operation == "*":
    if firstNum == 45 and operation == "*" and secondNum == 3:
        result = 555
    else:
        result = firstNum * secondNum 
else:
    print('No')


print(result)
