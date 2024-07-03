# CIS41 Jihye Choi
# Final Part 1

from PrintFile import PrintFile

if __name__ == "__main__":
    while True:
        order = PrintFile()
        order.get_inputs()
        order.save_to_file()
        if order._exit_flag:
            break
        userInputToContinue = input("Continue for another order (Any key = Yes, n = No)? ")
        if userInputToContinue.lower() == 'n':
            print("The system is shutting down!")
            break

'''
********** De Anza Burger **********
1    De Anza Burger      $5.25
2    Bacon Cheese        $5.75
3    Mushroom Swiss      $5.95
4    Western Burger      $5.95
5    Don Cali Burger     $5.95

Enter your choice between 1-5 or 6 to exit: 6
End of your order!
Continue for another order(Any keys= Yes, n= No)?n
The system is shutting down!

---------------------------------------------------------
********** De Anza Burger **********
1    De Anza Burger      $5.25
2    Bacon Cheese        $5.75
3    Mushroom Swiss      $5.95
4    Western Burger      $5.95
5    Don Cali Burger     $5.95

Enter your choice between 1-5 or 6 to exit: 2
How many do you want: 3

Enter 1 for staff or 2 for student: 1

Your Bill: 
Item:             Bacon Cheese
Quantity:                    3
Cost                    $17.25
Before Tax              $17.25
Tax amount               $1.55
Total Price             $18.80

Enter your choice between 1-5 or 6 to exit: 6
End of your order!
Continue for another order(Any keys= Yes, n= No)?n
The system is shutting down!

********** De Anza Burger **********
1    De Anza Burger      $5.25
2    Bacon Cheese        $5.75
3    Mushroom Swiss      $5.95
4    Western Burger      $5.95
5    Don Cali Burger     $5.95

Enter your choice between 1-5 or 6 to exit: 2
How many do you want: 3

Enter 1 for staff or 2 for student: 2

Your Bill: 
Item:             Bacon Cheese
Quantity:                    3
Cost                    $17.25
Before Tax              $17.25
Tax amount               $0.00
Total Price             $17.25

Enter your choice between 1-5 or 6 to exit: 6
End of your order!

'''

