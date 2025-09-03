# Railway Ticket Fare:

# Age < 5 → Free

# Age 5–12 → Half ticket

# Age 13–60 → Full ticket

# Age > 60 → 30% concession.

# Prograam: 

age=int(input("Please enter your age:  "))
ticket=1000
if (age in range (0,5)):
    print("Congratulation's your ticket is free")
    print("Age: ",age,)
    print("Ticket Fare: ",ticket*0)
elif age in range(5,13):
    a=ticket*1/2
    print("Congratulation's your ticket will be Half")
    print("Age: ",age,)
    print("Ticket Fare: ",a)
elif age in range(13,61):
    print("Congratulation's your ticket is booked sucessfully")
    print("Age: ",age,)
    print("Ticket Fare: ",ticket)
elif age>=60:
    b=ticket-ticket*0.3
    print("Congratulation's you get '30%' concession in ticket")
    print("Age: ",age,)
    print("Ticket Fare: ",b)
else:
    print("Error")