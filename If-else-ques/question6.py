# Input a number and check if it is a Harshad Number (divisible by sum of digits).
num = int(input("Enter a number: ")) #15
sum=0 
temp = num 
while temp>0:
    d=temp%10
    sum=sum+d
    temp=temp//10

print(d)
if num % d == 0:
    print("Harshad")
else:
    print("Non Harshad")

