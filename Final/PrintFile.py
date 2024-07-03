# CIS41 Jihye Choi
# Final Part 1

from OrderBurger import OrderBurger
import datetime
import time

class PrintFile(OrderBurger):
    def __init__(self):
        super().__init__()

    def save_to_file(self):
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp = orderTimeStamp + '.txt'
        try:
            outfile = open(orderTimeStamp, "w")
            for i in self._BURGERS:
                if self._burgersDict[i] != 0: 
                    outfile.write('{:<15s}{:>15s}'.format('Item: ', i) + "\n")
                    outfile.write('{:<15s}{:>15d}'.format('Quantity : ', self._burgersDict[i]) + "\n")
                    outfile.write('{:<15s}{:>15s}'.format('Cost ', '$' + str('{:.2f}'.format(self._before_tax))) + "\n")
                    outfile.write('{:<15s}{:>15s}'.format('Before Tax ', '$' + str('{:.2f}'.format(self._before_tax))) + "\n")
                    outfile.write('{:<15s}{:>15s}'.format('Tax amount ', '$' + str('{:.2f}'.format(self._tax_amount))) + "\n")
                    outfile.write('{:<15s}{:>15s}'.format('Total Price ', '$' + str('{:.2f}'.format(self._total_price))) + "\n")
                    outfile.close()
        except(IOError):
            print('Error creating the file')   