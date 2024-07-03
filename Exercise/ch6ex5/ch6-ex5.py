#CIS41 - Jihye Choi
#Validate company and calculate pay using module

from module import *

def payProcess():
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)

payProcess()


'''
What is your company name?: ha
Input valid company name!
What is your company name?: Amazon
Enter the hours: 40
Enter the rate: 10
The total pay is: $400.0

What is your company name?: Facebook
Enter the hours: 45
Enter the rate: 10
The total pay is: $475.0
'''
