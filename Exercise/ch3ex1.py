#CIS 41 - Jihye Choi
#Write a program to prompt the user for hours and rate per hour to compute gross pay
#1.5 times the hourly rate for hour worked above 40 hours

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

pay = hours * rate
overtime = (40 * rate) + ((hours - 40) * rate * 1.5)

if hours < 40:
    print(f"Pay: {pay: .2f}")
else: 
    print(f"Pay: {overtime: .2f}")

'''
Enter hours: 45
Enter rate: 10
Pay:  475.00

Enter hours: 40
Enter rate: 10
Pay:  400.00

'''