#CIS41 - Jihye Choi
#write your code to validate the inputs and 
#keep asking the user to enter valid inputs for the hours and the rate value

from random import randint

while True:
    company = input("Enter your company name:")
    if(company == ""):
        print("Enter your company name:") 
        
    else:
        companyName = company.strip()
        rate = float(input("Enter the rate:"))
        
        if rate <= 0:
            print("Enter Positive Number!")
        else:
            hours = float(input("Enter the hours:"))
            if(hours > 40):
                pay = (rate * 40) + ((rate * 1.5) * (hours - 40))
            else:
                pay = rate * hours
            randomNumber = randint(1000,2000)
            print("Company:", companyName)
            print("Hours:", hours)
            print("Rate:", rate) 
            print("*"*30)    
            print("Your document number is:", randomNumber)
            print("Your ", companyName, " gross pay is ", pay, " dollars.")
        break  

'''
Company: Amazon
Hours: 50.0
Rate: 500.0
******************************
Your document number is: 1486
Your  Amazon  gross pay is  27500.0  dollars.

Company: Apple
Hours: 45.0
Rate: 10.0
******************************
Your document number is: 1896
Your  Apple  gross pay is  475.0  dollars.

Enter your company name:Apple 
Enter the rate:-1
Enter Positive Number!
'''