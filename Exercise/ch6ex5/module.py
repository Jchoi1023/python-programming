#CIS40 - Chapter6 Exercise 5 - Jihye Choi
#Validate company and calculate pay using module

COMPANYLIST = ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']

def get_input():
    while True:
        company = input("What is your company name?: ")
        companyName = company.strip()
        if companyName in COMPANYLIST:
            hours = float(input("Enter the hours: "))
            rate = float(input("Enter the rate: "))
            if rate < 0 or hours < 0:
                print("Enter valid number")
                hours = float(input("Enter the hours: "))
                rate = float(input("Enter the rate: "))
            return hours, rate
        else:
            print("Input valid company name!")

def compute_pay(hours, rate):
    if(hours <= 40):
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    return pay        

def print_output(pay):
    print(f"The total pay is: ${pay}")

