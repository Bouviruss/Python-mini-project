print("BASIC CALCULATOR WITH PYTHON")
num1 = float (input("Write your First number: "))
oper = input("Write your operator is : ")
num2 = float (input("Write your Second number: "))

if oper == "+":
    print (num1 + num2)
elif oper == "-":
    print (num1 - num2)
elif oper == "*":
    print (num1 * num2)
elif oper == "/":
    print (num1 / num2)

else:
    print("wrong operator please try again: ")