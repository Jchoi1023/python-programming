from Burger import Burger
import sys

class OrderBurger(Burger):
    def __init__(self):
        super().__init__()
        self._tax = 0.09
        self._before_tax = 0
        self._total_price = 0
        self._tax_amount = 0

    def get_inputs(self):
        checker1 = True
        self.show_menu()
        while checker1:
            try:
                order = int(input('\nEnter your choice between 1-5 or 6 to exit: '))
                if order < 1 or order >6:
                    print("Invalid choice! Please enter an integer between 1-6!")
                elif order == 6:
                    print('End of your order!')
                    # checker1 = False
                    return
                else:
                    checker2 = True
                    while checker2:
                        try:
                            number = int(input('How many do you want: '))
                            if number < 0:
                                print('Invalid choice! Please enter a positive number!')
                            else:
                                key = self._BURGERS[order - 1]
                                self._burgersDict[key] += number
                                checker2 = False
                        except:
                            print('Please enter a numeric integer!')
            except:
                print('Please enter a numeric Integer!')

        
    def compute_bill(self):
        for i in self._BURGERS:
            self._before_tax += self._burgersDict[i] * self._priceDict[i]
        checker3 = True
        while checker3:
            try:
                id = int(input('\nEnter 1 for staff or 2 for student: '))
                if id < 1 or id > 2:
                    print('Invalid choice! Please enter 1 or 2!')
                elif id == 1:
                    self._tax_amount = self._tax * self._before_tax
                    self._total_price = self._before_tax + self._tax_amount
                    checker3 = False
                elif id == 2:
                    self._total_price = self._before_tax
                    checker3 = False
            except:
                print('Please enter a numeric integer!')


    def print_bill(self):
        print()
        print('Your Bill: ')
        for i in self._BURGERS:
            if self._burgersDict[i] != 0:
                print('{:<15s}{:>15s}'.format('Item: ', i))
                print('{:<15s}{:>15d}'.format('Quantity: ', self._burgersDict[i]))
        print('{:<15s}{:>15s}'.format('Cost ', '$' + str('{:.2f}'.format(self._before_tax))))
        print('{:<15s}{:>15s}'.format('Before Tax ', '$' + str('{:.2f}'.format(self._before_tax))))
        print('{:<15s}{:>15s}'.format('Tax amount ', '$' + str('{:.2f}'.format(self._tax_amount))))
        print('{:<15s}{:>15s}'.format('Total Price ', '$' + str('{:.2f}'.format(self._total_price))))       
        