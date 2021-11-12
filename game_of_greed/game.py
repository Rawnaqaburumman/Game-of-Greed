from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
import collections

class Game:
    gameBank= Banker()
    def __init__(self, roller=None): 
        self.roller=roller or GameLogic.roll_dice
        self.round = 1
        self.number_of_dice = 6
        self.total=0

    def roll_dice_play(self):
        print(f'Rolling {self.number_of_dice} dice...')
        dice = self.roller(self.number_of_dice) or GameLogic.roll_dice(self.number_of_dice)
        print(dice)
        printableDice = ','.join([str(d) for d in dice])
      
        print(printableDice)
        self.zilch(dice)
        keepOrQuit = input("Enter dice to keep (no spaces), or (q)uit: ")
        if keepOrQuit == 'q': self.userQuit()
        else:
            if collections.Counter ([char for char in keepOrQuit])['5']> collections.Counter ([char for char in printableDice])['5']: 
                print ('Cheater!!! Or possibly made a typo...')
                print (printableDice)
                keepOrQuit = input("Enter dice to keep (no spaces), or (q)uit: ")
            self.number_of_dice -= len(keepOrQuit)
            userChoice = self.user_choice_to_tuple(keepOrQuit)
            self.gameBank.shelf(userChoice)
            print(f'You have {self.gameBank.shelved} unbanked points and {self.number_of_dice} dice remaining')
            userInput22 = input('(r)oll again, (b)ank your points or (q)uit ')
            self.userChoTwo(userInput22)

    def user_choice_to_tuple(self,userInput):
            List=list(userInput)
            intValue=[int(x)for x in List ]
            rollingScore=GameLogic.calculate_score(tuple(intValue))
            return rollingScore

    def userQuit(self):
        if self.gameBank.balance != 0 or self.gameBank.shelved !=0 :
            print(f"Total score is {self.gameBank.balance} points")
        print(f'Thanks for playing. You earned {self.gameBank.balance} points')
        totalOfAll = self.gameBank.balance
        self.total=self.gameBank.balance
        self.gameBank.balance =0
        self.gameBank.shelved = 0
        self.round = 0

    def userChoTwo(self,userChoice):
        if userChoice == 'r':
                self.roll_dice_play()
        elif userChoice =='b':
            self.number_of_dice = 6
            print(f'You banked {self.gameBank.shelved} points in round {self.round}')
            self.gameBank.bank()
            print(f'Total score is {self.gameBank.balance} points')
            self.total=self.gameBank.balance
            self.round+=1
            self.rolling()
        elif userChoice == 'q':
            self.userQuit()

    def rolling(self):
        print(f'Starting round {self.round}')
        self.roll_dice_play()
        
              
    def play(self):
        print("Welcome to Game of Greed")
        userInput = input("Wanna play? ")
        if userInput == 'n':
            print("OK. Maybe another time")
            pass
        else:
            self.rolling()

    
    def zilch(self,value):
        zilch_6 = collections.Counter (value)[6]
        zilch_3 = collections.Counter (value)[4]
        zilch_4 = collections.Counter (value)[3]
        zilch_2 = collections.Counter (value)[2]
        if (1 not in value and 5 not in value) and (zilch_6 <3 and zilch_3 <3 and zilch_4 <3 and zilch_2 <3):
           print ('Zilch!!! Round over')
           print (f'You banked 0 points in round {self.round}')
           print(f'Total score is {self.gameBank.balance} points')
           self.number_of_dice = 6
           self.round+=1
           self.gameBank.clear_shelf()
           self.rolling()

if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
    # game.zilch((4,))