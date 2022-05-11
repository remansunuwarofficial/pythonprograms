#problem 1
'''
Own dictionary
Create a dictionary and take input from the user and return the meaning of the
from your dictionary
'''
dictionary = {
    "url": "Universal Resource Locator",
    "attest": "provide proof of",
    "audio": "sound",
    "yak": "an animal"
}
usersKey = input("Enter a Word ")

print(dictionary[usersKey])


#problem 2
'''
faulty Calculator
Design a calculator which will correctly solve all the problems except following problems
(45 * 3 = 555, 56  + 9 = 77, 56 / 6 = 4)
'''
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


