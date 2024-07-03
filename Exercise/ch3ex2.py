#CIS 41 - Jihye Choi
#Write a program to prompt the user for hours and rate per hour to compute gross pay
#1.5 times the hourly rate for hour worked above 40 hours
#Use isdigit

hours = input("Enter hours: ")
if hours.isdigit(): 
    rate = input("Enter rate: ")
    if rate.isdigit():
        pay = int(hours) * int(rate)
        overtime = (40 * int(rate)) + ((int(hours) - 40) * int(rate) * 1.5)
        if int(hours) < 40:
            print(f"Pay: {pay: .2f}")
        else: 
            print(f"Pay: {overtime: .2f}")
    else:
        print("Error, please enter numeric input.")
else:
    print("Error, please enter numeric input.")


'''
Enter hours: 45
Enter rate: 10
Pay:  475.00

Enter hours: 45
Enter rate: e
Error, please enter numeric input.

Enter hours: e
Error, please enter numeric input.
'''