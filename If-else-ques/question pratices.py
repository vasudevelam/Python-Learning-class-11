#wap to check a number is divisible by both 3  and 7
num1=float(input("enter a number is:  "))
d=num1%3==0
c=num1%7==0
if (num1%3==0):
    print("print numbwer:  ",num1,"divisible by 3 is:  ",d)
elif (num1%7==0):
    print("Print number:  ",num1,"divisible by 7 is:  ",c)
else:
    print("print number:  ",num1,"not divisible both 3 and 7")
