# Input an amount and print the number of currency notes (₹2000, ₹500, ₹200, ₹100, ₹50, ₹20, ₹10).

amount=float(input("Enter number"))
a=amount//2000
amount=amount%2000
b=amount//500
amount=amount%500
c=amount//200
amount=amount%200
e=amount//100
amount=amount%100
f=amount//50
amount=amount%50
t=amount//20
amount=amount%20
y=amount//10
amount=amount%10
print(a)
print(b)
print(c)
print(e)
print(f)
print(t)
print(y)




