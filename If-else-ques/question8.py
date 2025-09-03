#wap to input age and gender person aligible for army join condition is male 18-25 fem 18-23
age =int(input("Enter a AGE is: "))
gender =input("Enter a GENDER is:  ")
if gender == "MALE" :
    if age in range(18,26):
        print("Eligble")
    else:
        print("Not Eligble")
elif gender == "FEMALE" :
    if age in range(18,24):
        print("Eligble")
    else:
        print("Not Eligble")
elif gender!="MALE"or "FEMALE":
    print("Kindly enter 'MALE' OR 'FEMALE' ")