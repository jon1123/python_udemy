# Class players hand: stand, hit, (double down, Later)
# class game outcome: win, lose
#class players money: Money starting, addin, lost, betting
class Money(object):
    '''This is for ckeeping tack of all tansactions'''
    def __init__(self,money= 1000):
        self.money = money
        
    def betting_amount(self, betting):
        self.betting = betting
        self.money -= betting
        print("You have bett: $"+str(betting)+". Your new curent balancs is: $" + str(self.money))
       
       ''' Not working yet
    def calu_winings(self, betting):
        global won = 2 * self.betting
        
    
    def add_winings(self, betting):
        
        self.money += won
        print("You have won: $"+str(won)+". Your curent balancs is: $" + str(self.money))  '''
        
    def cunrent_money(self):
        print("Your curent balancs is: $" + str(self.money))
 
    # lost is not subtracted due to betting lost is told at time of lost hand

# the deck
# deck can be A,1,2,3,4,5,6,7,8,9,10,J,Q,K in Clubs,Spads, Dimonds, Harts
# class dealers hand and rquirments


"""
Milestone Project 2 - Blackjack Game
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the players total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game. You can not just use functions in your game.
Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
Feel free to expand this game-try including multiple players. Try adding in Double-Down and card splits!
Remember to you are free to use any resources you want and as always:

HAVE FUN!
"""