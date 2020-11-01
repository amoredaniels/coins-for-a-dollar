#Amore' Daniels

#import random module
import random

# Create a coin class
class Coin():
  #make a list for random choices
    sides = ['Heads','Tails']
# define attributes
    def __init__(self,name,value):
        self.name = name
        self.value = value
        #anything made in the class is an attribute
        self.side = 'Tails'

#define setters
    def setName(self,name):
        self.name = name
    def setValue(self,value):
        self.value = value
#set side attribute to a random choice from the list
    def setSide(self):
        self.side = random.choice(Coin.sides)

#these are behaviours/getters/methods bc they return a value
    def getName(self):
        return self.name
    def getSide(self):
        return self.side
    def getValue(self):
        return self.value

#print coins and their sides using __str__ method
    def __str__(self):
        return ('Here are the sides:\n{}:{}'.format(self.name,self.side))
    
#def main function
def main():
    # initialize a sum/total/result to 0.0
    balance = 0.00
    # create instances of the coin class for each coin
    #(pass appropriate arguments)
    quarter = Coin('Quarter',0.25)
    dime = Coin('Dime',0.10)
    nickel = Coin('Nickel',0.05)
    # while or as long as the total is < 1.00
    while balance < 1.00:
    #randomly pick between heads or tails
        quarter.setSide()
        dime.setSide()
        nickel.setSide()
        #if random choice is heads add the appropriate value to balance
        if quarter.side == 'Heads':
            balance += quarter.getValue()
        if nickel.side == 'Heads':
            balance += nickel.getValue()
        if dime.side == 'Heads':
            balance += dime.getValue()
        #print updated total
        print('Sum balance: ${:.2f}\n'.format(balance))
        print('tossing the coins...\n')
        #print all the instances
        print(quarter)
        print(nickel)
        print(dime)
        print('---------------------')

    # if total = 1.00 print you win
    if balance == 1.00:
        print('You win!')
    # if total > 1.00 print you lose
    if balance > 1.00:
        print('Game over.You lose.')
#call main
main()
