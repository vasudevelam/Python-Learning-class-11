# Write a program to check whether a number is odd or even without using modulus % operator.

#program:

num = int(input("Enter a number: "))
if (num==0):
    print("Number is zero")
elif (num%2==0):
    print ("Number is even")
elif (num%2!=0):
    print ("Number is Odd")
