#Jihye Choi
#CIS41 Midterm Part 1
#Calculate and show the result for the process of an order of hamburger

import sys
#Menu & Prices
MENU_1="1. De Anza Burger"
MENU_2="2. Bacon Cheese"
MENU_3="3. Mushroom Swiss"
MENU_4="4. Western Burger"
MENU_5="5. Don Cali Burger"
PRICE_1=5.25
PRICE_2=5.75
PRICE_3=5.95
PRICE_4=5.95
PRICE_5=5.95
TAX=0.09

#Function for whole ordering process 
def main():
    displayMenu()
    quantity1, quantity2, quantity3, quantity4, quantity5, status = getInput()
    priceBeforeTax, priceAfterTax = computeBill(quantity1, quantity2, quantity3, quantity4, quantity5, status)
    displayBill(quantity1, quantity2, quantity3, quantity4, quantity5, status, priceBeforeTax, priceAfterTax)

#Show the menu
def displayMenu():
    print("================ De Anza College Food Court ================")
    print(MENU_1,"..........$",PRICE_1)
    print(MENU_2,"..........$",PRICE_2)
    print(MENU_3,"..........$",PRICE_3)
    print(MENU_4,"..........$",PRICE_4)
    print(MENU_5,"..........$",PRICE_5)
    print("6. Exit")

#Get an order: Choose menu and quantity
def getInput():
    quantity1 = 0
    quantity2 = 0
    quantity3 = 0
    quantity4 = 0
    quantity5 = 0
    
    while True:
        order=input("What burger do you want to order?(Enter a number from 1 to 5 ot 6 to exit)")
        if(order.isdigit()):
            order=int(order)   
            if order > 0 and order < 6:
                quantity = input("Enter how many burger do you want?")
                if(quantity.isdigit()):
                    quantity=int(quantity)
                    if order == 1:
                        quantity1 += quantity
                    elif order == 2:
                        quantity2 += quantity
                    elif order == 3:
                        quantity3 += quantity
                    elif order == 4:
                        quantity4 += quantity
                    elif order == 5:
                        quantity5 += quantity
                else:
                    print("Enter valid number!")
                    quantity = input("Enter how many burger do you want?")            
            elif order == 6:
                sys.exit("Exit")                                                                 
            else:
                print("Enter a valid number between 1 and 6!")
                continue
        else:
            print("Enter valid number!")
            continue
        #student or staff
        status = int(input("Are you a student or a staff? (Enter student = 0 or staff = 1)"))
        return quantity1, quantity2, quantity3, quantity4, quantity5, status  

# Calculate a bill
def computeBill(quantity1, quantity2, quantity3, quantity4, quantity5, status):
    priceBeforeTax= quantity1 * PRICE_1 + quantity2 * PRICE_2 + quantity3 * PRICE_3 + quantity4 * PRICE_4 + quantity5 * PRICE_5   
    priceAfterTax = priceBeforeTax + priceBeforeTax*status*TAX     
    return priceBeforeTax, priceAfterTax          


#Print the bill
def displayBill(quantity1, quantity2, quantity3, quantity4, quantity5, status, priceBeforeTax, priceAfterTax ):
    if quantity1 != 0:
        print("The food items: ", MENU_1,"\n",
            "The quantities: ", quantity1,"\n",
            "The cost of them: $",PRICE_1,"\n", 
            "The total before tax: $", round(priceBeforeTax, 2), "\n",
            "Tax amount: $", round(priceBeforeTax*status*TAX,2), "\n",
            "Total price after tax: $", round(priceAfterTax,2))
    elif quantity2 !=0:
        print("The food items: ", MENU_2,"\n",
            "The quantities: ", quantity2,"\n",
            "The cost of them: $",PRICE_2,"\n",
            "The total before tax: $", round(priceBeforeTax, 2), "\n",
            "Tax amount: $", round(priceBeforeTax*status*TAX,2), "\n",
            "Total price after tax: $", round(priceAfterTax,2))
    elif quantity3 !=0:
        print("The food items: ", MENU_3,"\n",
            "The quantities: ", quantity3,"\n",
            "The cost of them: $",PRICE_3,"\n",
            "The total before tax: $", round(priceBeforeTax, 2), "\n",
            "Tax amount: $", round(priceBeforeTax*status*TAX,2), "\n",
            "Total price after tax: $", round(priceAfterTax,2))
    elif quantity4 !=0:
        print("The food items: ", MENU_4,"\n",
            "The quantities: ", quantity4,"\n",
            "The cost of them: $",PRICE_4,"\n",
            "The total before tax: $", round(priceBeforeTax, 2), "\n",
            "Tax amount: $", round(priceBeforeTax*status*TAX,2), "\n",
            "Total price after tax: $", round(priceAfterTax,2))
    elif quantity5 !=0:
        print("The food items: ", MENU_5,"\n",
            "The quantities: ", quantity5,"\n",
            "The cost of them: $",PRICE_5,"\n",
            "The total before tax: $", round(priceBeforeTax, 2), "\n",
            "Tax amount: $", round(priceBeforeTax*status*TAX,2), "\n",
            "Total price after tax: $", round(priceAfterTax,2))

main()

'''
================ De Anza College Food Court ================
1. De Anza Burger ..........$ 5.25
2. Bacon Cheese ..........$ 5.75
3. Mushroom Swiss ..........$ 5.95
4. Western Burger ..........$ 5.95
5. Don Cali Burger ..........$ 5.95
6. Exit
What burger do you want to order?(Enter a number from 1 to 5 ot 6 to exit)6
Exit

================ De Anza College Food Court ================
1. De Anza Burger ..........$ 5.25
2. Bacon Cheese ..........$ 5.75
3. Mushroom Swiss ..........$ 5.95
4. Western Burger ..........$ 5.95
5. Don Cali Burger ..........$ 5.95
6. Exit
What burger do you want to order?(Enter a number from 1 to 5 ot 6 to exit)-1
Enter valid number!
What burger do you want to order?(Enter a number from 1 to 5 ot 6 to exit)


================ De Anza College Food Court ================
1. De Anza Burger ..........$ 5.25
2. Bacon Cheese ..........$ 5.75
3. Mushroom Swiss ..........$ 5.95
4. Western Burger ..........$ 5.95
5. Don Cali Burger ..........$ 5.95
6. Exit
What burger do you want to order?(Enter a number from 1 to 5 ot 6 to exit)3
Enter how many burger do you want?5
Are you a student or a staff? (Enter student = 0 or staff = 1)1
The food items:  3. Mushroom Swiss 
The quantities:  5 
The cost of them: $ 5.95 
The total before tax: $ 29.75 
Tax amount: $ 2.68 
Total price after tax: $ 32.43

================ De Anza College Food Court ================
1. De Anza Burger ..........$ 5.25
2. Bacon Cheese ..........$ 5.75
3. Mushroom Swiss ..........$ 5.95
4. Western Burger ..........$ 5.95
5. Don Cali Burger ..........$ 5.95
6. Exit
What burger do you want to order?(Enter a number from 1 to 5 ot 6 to exit)5
Enter how many burger do you want?10
Are you a student or a staff? (Enter student = 0 or staff = 1)0
The food items:  5. Don Cali Burger 
The quantities:  10 
The cost of them: $ 5.95 
The total before tax: $ 59.5 
Tax amount: $ 0.0 
Total price after tax: $ 59.5

'''