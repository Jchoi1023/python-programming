# CIS41 Jihye Choi
# Final Part 1

class Burger():
    def __init__(self):
        self._burgersDict = {"De Anza Burger":0, "Bacon Cheese":0, "Mushroom Swiss":0, "Western Burger":0, "Don Cali Burger":0}
        self._priceDict = {"De Anza Burger":5.25, "Bacon Cheese":5.75, "Mushroom Swiss":5.95, "Western Burger":5.95, "Don Cali Burger":5.95}
        self._PRICES =[5.25, 5.75, 5.95, 5.95, 5.95]
        self._BURGERS = ["De Anza Burger", "Bacon Cheese", "Mushroom Swiss", "Western Burger", "Don Cali Burger"]

    def show_menu(self):
        print('********** De Anza Burger **********')
        for i in range(len(self._BURGERS)): 
            print('{:<5d}{:<15s}{:>10s}'.format(i + 1, self._BURGERS[i], '$' + str(self._PRICES[i])))