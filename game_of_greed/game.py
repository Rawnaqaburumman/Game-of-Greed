from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
import collections
#pycharm
class Game:
    gameBank= Banker()

    def __init__(self, roller=None): 
        self.roller, self.round = roller, 1
        self.number_of_dice = 6
        self.total = self.gameBank.balance

    def roll_dice_play(self):
        print(f'Rolling {self.number_of_dice} dice...')
        dice = self.roller(self.number_of_dice) or GameLogic.roll_dice(self.number_of_dice)
        printableDice = ','.join([str(d) for d in dice])
        print(printableDice)

        if Game.zilch(dice):
           print ('Zilch!!! Round over')
           print (f'You banked 0 points in round {self.round}')
           print(f'Total score is {self.gameBank.balance} points')
           self.number_of_dice = 6
           self.round+=1
           self.rolling()
        else:
            keepOrQuit = input("Enter dice to keep (no spaces), or (q)uit: ")
            if keepOrQuit == 'q': self.userQuit()
            else:
                while ( 
                   collections.Counter ([char for char in keepOrQuit])['1']> collections.Counter ([char for char in printableDice])['1'] or
                   collections.Counter ([char for char in keepOrQuit])['2']> collections.Counter ([char for char in printableDice])['2'] or
                   collections.Counter ([char for char in keepOrQuit])['3']> collections.Counter ([char for char in printableDice])['3'] or
                   collections.Counter ([char for char in keepOrQuit])['4']> collections.Counter ([char for char in printableDice])['4'] or
                   collections.Counter ([char for char in keepOrQuit])['5']> collections.Counter ([char for char in printableDice])['5'] or
                   collections.Counter ([char for char in keepOrQuit])['6']> collections.Counter ([char for char in printableDice])['6']) : 
                        print ('Cheater!!! Or possibly made a typo...')
                        print (printableDice)
                        keepOrQuit = input("Enter dice to keep (no spaces), or (q)uit: ")
                        if keepOrQuit == 'q': break
                if keepOrQuit == 'q': self.userQuit()
                else:       
                    self.number_of_dice -= len(keepOrQuit)
                    userChoice = 0
                    if set ([int(x) for x in list (keepOrQuit)]) >= set ([2,1,6,5,4,3]): userChoice += 1500 
                    elif len(keepOrQuit)==6 and max (dict (collections.Counter([char for char in keepOrQuit])).values()) == 2: userChoice += 1500
                    else:
                        userChoice += self.user_choice_to_tuple([1] * collections.Counter(keepOrQuit)['1'])
                        userChoice += self.user_choice_to_tuple([2] * collections.Counter(keepOrQuit)['2'])
                        userChoice += self.user_choice_to_tuple([3] * collections.Counter(keepOrQuit)['3'])
                        userChoice += self.user_choice_to_tuple([4] * collections.Counter(keepOrQuit)['4'])
                        userChoice += self.user_choice_to_tuple([5] * collections.Counter(keepOrQuit)['5'])
                        userChoice += self.user_choice_to_tuple([6] * collections.Counter(keepOrQuit)['6'])
                    self.gameBank.shelf(userChoice)
                    print(f'You have {self.gameBank.shelved} unbanked points and {self.number_of_dice} dice remaining')
                    userInput22 = input('(r)oll again, (b)ank your points or (q)uit ')
                    if userChoice == 1500: self.number_of_dice = 6
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

    def zilch(value):
        zilch_6 = collections.Counter (value)[6]
        zilch_3 = collections.Counter (value)[4]
        zilch_4 = collections.Counter (value)[3]
        zilch_2 = collections.Counter (value)[2]
        if (1 not in value and 5 not in value) and (zilch_6 <3 and zilch_3 <3 and zilch_4 <3 and zilch_2 <3):
           return True

if __name__ == "__main__":
    # game = Game(GameLogic.roll_dice)
    # game.play()
    print (('Thanks for playing. You earned 1550 points'.replace('Thanks for playing. You earned ','')).replace(' points',''))

