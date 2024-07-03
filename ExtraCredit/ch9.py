#CIS41 Jihye Choi
#Chapter 9 - Extra Credit
#Write a class bug

class Bug:
    def __init__(self, initialPosition):
        self.position = initialPosition
        self.direction = 1 

    def move(self):
        self.position += self.direction

    def turn(self):
        self.direction *= -1

    def getPosition(self):
        return self.position

bugsy = Bug(10)  
bugsy.move()
print(f"Now the position is {bugsy.getPosition()}")
bugsy.turn()
bugsy.move()
print(f"Now the position is {bugsy.getPosition()}")

'''
Now the position is 11
Now the position is 10
'''