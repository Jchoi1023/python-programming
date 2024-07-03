#CIS 41 - Jihye Choi
# Write a program to prompt the user for hours and rate per hour to compute gross pay


hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate

print(f"Pay: {pay: .2f}")

'''
Enter hours: 4.6
Enter rate: 4
Pay:  18.40

Enter hours: 35
Enter rate: 2.75
Pay:  96.25
'''