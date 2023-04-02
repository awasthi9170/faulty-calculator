number=int(input("enter a number"))
number1=int(input("enter a another number"))
print("enter what you want'+',+,-,*,/")
number2=input()
if number==45 and number1==3 and number2=='*':
    print("555")
elif number==56 and number1==9 and number2=='+':
    print("76")
elif number==56 and number1==6 and number2=='/':
    print("4")
elif number2 == '+':
    add=number+number1
    print(add)
elif number2 == '*':
    mul=number*number1
    print(mul)
elif number2 == '-':
    sub=number-number1
    print(sub)
elif number2 == '/':
    div=number/number1
    print(div)




