# CIS41 - Jihye Choi
#Rewrite your pay computation with time-and-a-half for overtime and 
#create a function called compute_pay which takes two parameters ( hours and  rate).


def get_input():
    while True:
        hours = float(input("Enter the hours: "))
        rate = float(input("Enter the rate: "))
        if rate < 0 or hours < 0:
            print("Enter valid number")
            hours = float(input("Enter the hours: "))
            rate = float(input("Enter the rate: "))
        return hours, rate

def compute_pay(hours, rate):
    if(hours <= 40):
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    return pay        

def print_output(pay):
    print(f"The total pay is: ${pay}")

def main():
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)

main()

'''
Enter the hours: 40
Enter the rate: 3
The total pay is: $120.0

Enter the hours: 45
Enter the rate: 10
The total pay is: $475.0


'''